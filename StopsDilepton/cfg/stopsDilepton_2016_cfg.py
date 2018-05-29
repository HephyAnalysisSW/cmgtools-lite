# Heppy
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# General
import os

# Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

print "Year: 2016"

# general flags & settings 
minLeptons                  = 1
storePackedCandidates       = False
doElectronScaleCorrections  = False
doPhotonScaleCorrections    = False
keepLHEWeights              = getHeppyOption("keepLHEweights",True)
jsonAna.useLumiBlocks       = True
genAna.allGenTaus           = True

# Lepton settings
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.rhoMuon          = 'fixedGridRhoFastjetAll'
lepAna.rhoElectron      = 'fixedGridRhoFastjetAll'

# Electrons
lepAna.loose_electron_pt  = 5
lepAna.doMiniIsolation = True

lepAna.loose_electron_id  = ""
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = ""
lepAna.inclusive_electron_lostHits = 999.  # no cut
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

# Muons
# store everything
lepAna.loose_muon_pt  = 5
lepAna.inclusive_muon_dxy = 999.
lepAna.inclusive_muon_dz  = 999.
lepAna.inclusive_muon_eta = 999.
lepAna.inclusive_muon_id = None#   POG_ID_Loose
lepAna.inclusive_muon_pt = 0.

# rho area for both lepton flavors
lepAna.ele_isoCorr = "rhoArea"
lepAna.mu_isoCorr  = "rhoArea"
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'
lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'

# Loose selection 
lepAna.loose_electron_relIso = 0.5
lepAna.loose_muon_relIso     = 0.5

lepAna.match_inclusiveLeptons=True

if doElectronScaleCorrections:
    era = '25ns'
    lepAna.doElectronScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',

    'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',
    'gedelectron_p4combination_'+era),
    'isSync': False
    }
if doPhotonScaleCorrections:
    photonAna.doPhotonScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',
    'isSync': False
    }

# lepton skimming 
ttHLepSkim.minLeptons = minLeptons
ttHLepSkim.maxLeptons = 999

# jets & cleaning 
jetAna.minLepPt = 10
jetAna.recalibrateJets =  True
jetAna.jetPt = 15
jetAna.jetEta = 5.2 #FIXME
jetAna.addJECShifts = True
jetAna.doQG = False
jetAna.smearJets = False #should be false in susycore, already
jetAna.calculateSeparateCorrections = True #should be true if recalibrate, otherwise L1 inconsistent
jetAna.calculateType1METCorrection = True

# 2016/17 JEC
jetAna.applyL2L3Residual = "Data"
jetAna.dataGT = [ ( -1, "Summer16_23Sep2016BCDV3_DATA"), (276811, "Summer16_23Sep2016EFV3_DATA"), (278801, "Summer16_23Sep2016GV3_DATA"), (280385, "Summer16_23Sep2016HV3_DATA") ]
jetAna.mcGT   = "Summer16_23Sep2016V3_MC"

# tree Producer
from CMGTools.StopsDilepton.treeProducerStopsDilepton import *

# MET
metAna.recalibrate = "type1"
metAna.storePuppiExtra = False # False for MC, True for re-MiniAOD??
from CMGTools.TTHAnalysis.analyzers.chsMETAnalyzer import chsMETAnalyzer
chsMETAna = cfg.Analyzer(
    chsMETAnalyzer,
    maxDz=0.1,
    packedCandidates = 'packedPFCandidates',
    )
susyCoreSequence.append( chsMETAna )

# MET filters
from CMGTools.TTHAnalysis.analyzers.badChargedHadronAnalyzerSummer2016 import badChargedHadronAnalyzerSummer2016
badChargedHadronAna = cfg.Analyzer(
    badChargedHadronAnalyzerSummer2016, name = 'badChargedHadronAnaSummer2016',
    muons='slimmedMuons',
    packedCandidates = 'packedPFCandidates',
)
from CMGTools.TTHAnalysis.analyzers.badMuonAnalyzerSummer2016 import badMuonAnalyzerSummer2016
badMuonAna = cfg.Analyzer(
    badMuonAnalyzerSummer2016, name = 'badMuonAnaSummer2016',
    muons='slimmedMuons',
    packedCandidates = 'packedPFCandidates',
    minMuPt=100,
    postFix='',
)
susySingleLepton_globalVariables.extend( [
    NTupleVariable("Flag_badChargedHadronSummer2016",  lambda ev: ev.badChargedHadronSummer2016, int, help="badChargedHadron filter result"),
    NTupleVariable("Flag_badMuonSummer2016",  lambda ev: ev.badMuonSummer2016, int, help="badMuon filter result") ] )
susyCoreSequence.insert(susyCoreSequence.index(metAna),
                        badChargedHadronAna)
susyCoreSequence.insert(susyCoreSequence.index(metAna),
                        badMuonAna)

# iso tracks
isoTrackAna.setOff = False

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

# Fat jets
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
# SV
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)

#ISR jet counting
from CMGTools.TTHAnalysis.analyzers.nIsrAnalyzer import NIsrAnalyzer
nISRAna = cfg.Analyzer(
    NIsrAnalyzer, name="NIsrAnalyzer",
    minJets25 = 0,
    )
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        nISRAna)

if storePackedCandidates:
    from CMGTools.TTHAnalysis.analyzers.packedCandidateAnalyzer import packedCandidateAnalyzer
    packedCandidateAna = cfg.Analyzer(
        packedCandidateAnalyzer, name = 'packedCandidateAnalyzer',
        packedCandidates = 'packedPFCandidates',
    )
    susyCoreSequence.append( packedCandidateAna )

    susySingleLepton_collections.update( { "packedCandidates" : NTupleCollection("pf",     particleType, 15000, help="packed candidates (pf)")} )

# LHEAnalyzer
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig
lheWeightAna.usePSweights = True

# trigger bits
from CMGTools.StopsDilepton.triggers_2016 import triggerBits
triggerFlagsAna.triggerBits = triggerBits
trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    #processName = '',
    fallbackCollection = 'selectedPatTrigger',
    fallbackProcessName = 'PAT',
    unpackPathNames = True,
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu22_v*",1,0) or t.path("HLT_IsoTkMu22_v*",1,0) or t.path("HLT_IsoMu22_eta2p1_v*",1,0) or t.path("HLT_IsoTkMu22_eta2p1_v*",1,0) or t.path("HLT_IsoTkMu24_v*",1,0)  ],#"HLT_IsoMu22", "HLT_IsoTkMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22_eta2p1", "HLT_IsoMu24", "HLT_IsoTkMu24"
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.3,
    univoqueMatching = True,
    verbose = False,
)
trigMatcher1El = trigMatcher1Mu.clone(
    name="trigMatcher1El",
    label='1El',
    trgObjSelectors = [ lambda t : t.path("HLT_Ele27_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele25_eta2p1_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele27_eta2p1_WPLoose_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1Mu)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1El)

# store TTV lepton MVA in 2016 version
leptonTypeSusy.variables.append(  NTupleVariable("mvaTTV",lambda lepton : getattr(lepton, 'mvaValueTTV2016', -1), help="Lepton MVA (TTV 2016 version)") )

# tree producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusySingleLepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)

sequence = cfg.Sequence(
  susyCoreSequence+
      [
        LHEAna,
        ttHEventAna,
        treeProducer,
        ])

selectedComponents = [
        ]

if getHeppyOption("loadSamples"):
    from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    from CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.samples import *

    for sample in dataSamples:
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"

    # sync mc
    selectedComponents = [TTJets_SingleLeptonFromTbar]
    TTJets_SingleLeptonFromTbar.files=['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00A25ADE-DFD4-E611-8EAC-0025905A48B2.root']
    # sync data
    MuonEG_Run2016F_03Feb2017.files=["root://cms-xrd-global.cern.ch//store/data/Run2016F/MuonEG/MINIAOD/03Feb2017-v1/50000/0496325A-05EB-E611-953B-0025905A60DE.root"]
    selectedComponents += [MuonEG_Run2016F_03Feb2017]

    #selectedComponents = [ttZ0j_ll]
    #selectedComponents = [WZTo3LNu]
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        print comp.files
        comp.splitFactor = 10

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

preprocessorFile = "$CMSSW_BASE/python/CMGTools/StopsDilepton/preprocessor/runBTaggingSlimPreprocessor_cfg.py"
from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
preprocessor = CmsswPreprocessor(preprocessorFile)
jetAna.jetCol = 'selectedUpdatedPatJets'

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     preprocessor=preprocessor, 
                     events_class = event_class)

