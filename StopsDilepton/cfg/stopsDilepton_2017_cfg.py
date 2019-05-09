# Heppy
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# General
import os

# Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

print "Year: 2017"

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
lepAna.mu_effectiveAreas = 'Fall17'
lepAna.ele_effectiveAreas = 'Fall17'

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

# 2017 JEC
jetAna.applyL2L3Residual = "Data"
jetAna.dataGT = [ ( -1, "Fall17_17Nov2017B_V6_DATA"), ( 299337, "Fall17_17Nov2017C_V6_DATA"), ( 302030, "Fall17_17Nov2017D_V6_DATA"), ( 303435, "Fall17_17Nov2017E_V6_DATA"), ( 304911, "Fall17_17Nov2017F_V6_DATA") ]
jetAna.mcGT   = "Fall17_17Nov2017_V6_MC"

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
from CMGTools.StopsDilepton.triggers_2017 import triggerBits
triggerFlagsAna.triggerBits = triggerBits
trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    fallbackCollection = 'slimmedPatTrigger',
    fallbackProcessName = 'PAT',
    unpackPathNames = True,
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu27_v*",1,0) or t.path("HLT_IsoMu30_v*",1,0) ],
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.3,
    univoqueMatching = True,
    verbose = False,
)
trigMatcher1El = trigMatcher1Mu.clone(
    name="trigMatcher1El",
    label='1El',
    trgObjSelectors = [ lambda t : t.path("HLT_Ele27_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele32_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele35_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele38_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele40_WPTight_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1Mu)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1El)

# store TTV lepton MVA in 2017 version
leptonTypeSusy.variables.append(  NTupleVariable("mvaTTV",lambda lepton : getattr(lepton, 'mvaValueTTV2017', -1), help="Lepton MVA (TTV 2017 version)") )

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
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import *
    for sample in dataSamples:
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"

    #selectedComponents = [TTZToLLNuNu_amc_psw]
    selectedComponents = [T_tch]
    #selectedComponents = [WJetsToLNu_HT100to200]
    #selectedComponents = [MuonEG_Run2017F_17Nov2017]
   # T_tch.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8A9BD9C9-A042-E811-9D9D-7845C4FC35C9.root']
    #MuonEG_Run2017F_17Nov2017.json=None
    #MuonEG_Run2017F_17Nov2017.files = ["/afs/hephy.at/user/r/rschoefbeck/www/etc/pickevents.root"]
    #MuonEG_Run2017F_17Nov2017.files = ['root://cms-xrd-global.cern.ch//store/data/Run2018B/DoubleMuon/MINIAOD/PromptReco-v1/000/317/383/00000/F8DC8A54-1669-E811-8656-02163E01A01E.root']
    # sync
    #TTSemi_pow.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/50000/004C666D-C0E0-E711-AADB-0CC47A6C183A.root']
    #selectedComponents = [WWZ_4F]
    #MuonEG_Run2017F_17Nov2017.files=['root://cms-xrd-global.cern.ch//store/data/Run2017F/MuonEG/MINIAOD/17Nov2017-v1/50000/02F38D9F-54EA-E711-A28D-02163E014331.root']
    #selectedComponents += [MuonEG_Run2017F_17Nov2017]
    #selectedComponents = [TTZToLLNuNu_amc]
    #TTZToLLNuNu_amc.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/20000/02A1FA28-F1F9-E711-AFB2-002590E3A0FC.root']
    #selectedComponents = [ TTLep_pow ]
    #TTLep_pow.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v2/60000/0857E231-22EF-E711-BEAC-FA163E2DB7A6.root']
    #selectedComponents = [ GluGluToZZTo4mu ]

for comp in selectedComponents:
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

preprocessor = None

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     preprocessor=preprocessor, 
                     events_class = event_class)

