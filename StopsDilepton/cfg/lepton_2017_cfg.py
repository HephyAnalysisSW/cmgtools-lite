# Heppy
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# General
import os

# Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *
from CMGTools.StopsDilepton.AutoFillVectorTreeProducer  import * 
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

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
lepAna.pfCandAssocDR         = 0.5

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

#add pfCand variables
pfParticleType = NTupleObjectType("pfParticle", baseObjectTypes = [ particleType ], variables = [
NTupleVariable("puppiWeight",  lambda x : x.puppiWeight() if not abs(x.pdgId()) in [11,13] else 1., help="puppiWeight"),
NTupleVariable("hcalFraction",  lambda x : x.hcalFraction() if not abs(x.pdgId()) in [11,13] else 1., help="hcalFraction"),
NTupleVariable("fromPV",  lambda x : x.fromPV() if not abs(x.pdgId()) in [11,13] else 1., help="fromPV"),
NTupleVariable("dxy_pf",  lambda x : x.dxy(), help="dxy"),
NTupleVariable("dz_pf",  lambda x : x.dz(), help="dz"),
NTupleVariable("dzAssociatedPV",  lambda x : x.dzAssociatedPV() if not abs(x.pdgId()) in [11,13] else 1., help="dzAssociatedPV"),
NTupleVariable("deltaR",  lambda x : x.deltaR, help="deltaR to lepton"),
NTupleVariable("ptRel",  lambda x : x.ptRel, help="ptRel to lepton"),
])

# tree Producer
treeProducer = cfg.Analyzer(
     AutoFillVectorTreeProducer, name='treeProducer',
     vectorTree = False,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     globalVariables = [ ], # rho, nvertices, njets
     globalObjects = [], 
     collection = ( "selectedLeptons" , NTupleCollection("lep", leptonTypeSusy, 10, help="leptons after the preselection") ),
     vector_collections = [ 
        ( "pfCands_neutral" ,  NTupleCollection("pfCand_neutral", pfParticleType, 100, help="neutral pf candidates associated") ),
        ( "pfCands_charged" ,  NTupleCollection("pfCand_charged", pfParticleType, 100, help="charged pf candidates associated") ),
        ( "pfCands_photon" ,   NTupleCollection("pfCand_photon", pfParticleType, 100, help="photon pf candidates associated") ),
        ( "pfCands_electron" , NTupleCollection("pfCand_electron", pfParticleType, 100, help="electron pf candidates associated") ),
        ( "pfCands_muon" ,     NTupleCollection("pfCand_muon", pfParticleType, 100, help="muon pf candidates associated") ),
        ( "ivf",               NTupleCollection("SV",     svType, 20, help="SVs from IVF") ),
        ],
     defaultFloatType = 'F',
)

svType.variables.append( NTupleVariable("deltaR",  lambda x : x.deltaR, help="deltaR(v,lepton)"))

# add lepton classes
leptonTypeSusy.variables.append( NTupleVariable("isPromptId", lambda x: abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37], int, help="isPrompt for leptons after the preselection for MVA training"))
leptonTypeSusy.variables.append( NTupleVariable("isNonPromptId", lambda x: not (abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37]) and (abs(getattr(x,'mcMatchAny',-99)) in [4,5]), int,  help="isNonPrompt for leptons after the preselection for MVA training"))
leptonTypeSusy.variables.append( NTupleVariable("isFakeId", lambda x: not (abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37]) and not (abs(getattr(x,'mcMatchAny',-99)) in [4,5]), int,  help="isFake for leptons after the preselection for MVA training"))

#add INT-Type lepton variables as FLOAT (is default)
leptonTypeSusy.variables.append( NTupleVariable("convVeto_float", lambda x : x.passConversionVeto() if abs(x.pdgId())==11 else 1., help="Conversion veto (always true for muons)"))
leptonTypeSusy.variables.append( NTupleVariable("lostHits_float", lambda x : (x.gsfTrack() if abs(x.pdgId())==11 else x.innerTrack()).hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS), help="Number of lost hits on inner track"))

leptonTypeSusy.variables.append( NTupleVariable("trackerLayers_float", lambda x : (x.track() if abs(x.pdgId())==13 else x.gsfTrack()).hitPattern().trackerLayersWithMeasurement(), help="Tracker Layers") )
leptonTypeSusy.variables.append( NTupleVariable("pixelLayers_float", lambda x : (x.track() if abs(x.pdgId())==13 else x.gsfTrack()).hitPattern().pixelLayersWithMeasurement(), help="Pixel Layers") )
leptonTypeSusy.variables.append( NTupleVariable("trackerHits_float", lambda x : (x.track() if abs(x.pdgId())==13 else x.gsfTrack()).hitPattern().numberOfValidTrackerHits(), help="Tracker hits") )
leptonTypeSusy.variables.append( NTupleVariable("lostOuterHits_float",    lambda x : (x.gsfTrack() if abs(x.pdgId())==11 else x.innerTrack()).hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_OUTER_HITS), help="Number of lost hits on outer track") )
leptonTypeSusy.variables.append( NTupleVariable("nStations_float",    lambda lepton : float(lepton.numberOfMatchedStations()) if abs(lepton.pdgId()) == 13 else 4., help="Number of matched muons stations (4 for electrons)") )
leptonTypeSusy.variables.append( NTupleVariable("isTrackerMuon_float",   lambda x : x.physObj.isTrackerMuon() if abs(x.pdgId())==13 else 1, help="Muon is tracker") )

leptonTypeSusy.variables.append(  NTupleVariable("isElectron_float",lambda lepton : 1. if abs(lepton.pdgId())==11 else 0., help="isElectron") )
leptonTypeSusy.variables.append(  NTupleVariable("isMuon_float",lambda lepton : 1. if abs(lepton.pdgId())==13 else 0., help="isMuon") )

leptonTypeSusy.variables.append(  NTupleVariable("isGlobalMuon_float",   lambda x : x.physObj.isGlobalMuon() if abs(x.pdgId())==13 else 1., help="Muon is global"))
# store TTV lepton MVA in 2017 version
leptonTypeSusy.variables.append(  NTupleVariable("mvaTTV",lambda lepton : getattr(lepton, 'mvaValueTTV2017', -1), help="Lepton MVA (TTV 2017 version)") )

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
susyCoreSequence.insert(susyCoreSequence.index(lepAna),
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

    #selectedComponents = [MuonEG_Run2017F_17Nov2017]
    #MuonEG_Run2017F_17Nov2017.files = ["/afs/hephy.at/user/r/rschoefbeck/www/etc/pickevents.root"]
    #MuonEG_Run2017F_17Nov2017.files = ['root://cms-xrd-global.cern.ch//store/data/Run2018B/DoubleMuon/MINIAOD/PromptReco-v1/000/317/383/00000/F8DC8A54-1669-E811-8656-02163E01A01E.root']
    # sync
    #TTSemi_pow.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/50000/004C666D-C0E0-E711-AADB-0CC47A6C183A.root']
    #selectedComponents = [WWZ_4F]
    #MuonEG_Run2017F_17Nov2017.files=['root://cms-xrd-global.cern.ch//store/data/Run2017F/MuonEG/MINIAOD/17Nov2017-v1/50000/02F38D9F-54EA-E711-A28D-02163E014331.root']
    #selectedComponents += [MuonEG_Run2017F_17Nov2017]
    selectedComponents = [TTZToLLNuNu_amc]
    TTZToLLNuNu_amc.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/20000/02A1FA28-F1F9-E711-AFB2-002590E3A0FC.root']
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

