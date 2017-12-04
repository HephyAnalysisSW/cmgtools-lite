##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES         ##
## skim condition: >= 1 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# WTF?
jsonAna.useLumiBlocks = True

storePackedCandidates = False
####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'

lepAna.rhoMuon = 'fixedGridRhoFastjetAll'
lepAna.rhoElectron = 'fixedGridRhoFastjetAll'

## ELECTRONS
lepAna.loose_electron_pt  = 5
eleID = "Incl"
doElectronScaleCorrections = False
lepAna.doMiniIsolation = True

if eleID == "CBID":
  lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Veto" # no Iso
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 0.1
  lepAna.loose_electron_dz     = 0.2

  lepAna.inclusive_electron_id  = ""#"POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
  lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

elif eleID == "MVAID":
  inclusive_electron_id  = "" # same as in susyCore

  #lepAna.loose_electron_id = "POG_MVA_ID_Phys14_NonTrig_VLoose" # Phys14 era
  lepAna.loose_electron_id = "POG_MVA_ID_Spring15_NonTrig_VLoose" # Spring15 25ns era

elif eleID == "Incl": # as inclusive as possible
  lepAna.loose_electron_id  = ""
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 999.
  lepAna.loose_electron_dz     = 999.

  lepAna.inclusive_electron_id  = ""
  lepAna.inclusive_electron_lostHits = 999.  # no cut
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

## MUONS
# store everything
lepAna.inclusive_muon_dxy = 999.
lepAna.inclusive_muon_dz  = 999.
lepAna.inclusive_muon_eta = 999.
lepAna.inclusive_muon_id = None#   POG_ID_Loose
lepAna.inclusive_muon_pt = 0.

lepAna.loose_muon_pt  = 5

# Isolation
isolation = "relIso03"

if isolation == "miniIso":
  # do miniIso
  lepAna.doMiniIsolation = True
  lepAna.miniIsolationPUCorr = 'rhoArea'
  lepAna.miniIsolationVetoLeptons = None
  lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
  lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
  # normal relIso03
  lepAna.ele_isoCorr = "rhoArea"
  lepAna.mu_isoCorr = "deltaBeta"

  lepAna.loose_electron_relIso = 0.5
  lepAna.loose_muon_relIso = 0.5

if doElectronScaleCorrections:
    era = '25ns'
    lepAna.doElectronScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',

    'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',
    'gedelectron_p4combination_'+era),
    'isSync': False
    }

# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 1
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10
jetAna.recalibrateJets =  True 
jetAna.applyL2L3Residual = False #"Data"
jetAna.jetPt = 15
jetAna.jetEta = 5.2 #FIXME
jetAna.addJECShifts = True
jetAna.doQG = False
jetAna.smearJets = False #should be false in susycore, already

jetAna.calculateSeparateCorrections = True #should be true if recalibrate, otherwise L1 inconsistent
jetAna.calculateType1METCorrection = True

isFastSim = False

jetAna.dataGT = [ ( -1, "Summer16_23Sep2016BCDV3_DATA"), (276811, "Summer16_23Sep2016EFV3_DATA"), (278801, "Summer16_23Sep2016GV3_DATA"), (280385, "Summer16_23Sep2016HV3_DATA") ]
jetAna.mcGT   = "Summer16_23Sep2016V3_MC"

#jetAna.dataGT   = "80X_dataRun2_2016SeptRepro_v3"
#if isFastSim:
#    jetAna.mcGT   = "Spring16_FastSimV1_MC"
#else:
#    jetAna.mcGT   = "Summer16_23Sep2016V3_MC"

#JECdb = '/afs/hephy.at/work/d/dspitzbart/stops/CMSSW_8_0_25/src/CMGTools/RootTools/data/jec/Summer16_25nsV5_MC.db'

isTTDM = False
if isTTDM:
    susyCoreSequence.remove( triggerFlagsAna )

metAna.recalibrate = "type1"
metAna.storePuppiExtra = False # False for MC, True for re-MiniAOD??
#metAna.doTkMet = True # for chs met
from CMGTools.TTHAnalysis.analyzers.chsMETAnalyzer import chsMETAnalyzer
chsMETAna = cfg.Analyzer(
    chsMETAnalyzer,
    maxDz=0.1,
    packedCandidates = 'packedPFCandidates', 
    )
susyCoreSequence.append( chsMETAna )

## PHOTONS
doPhotonScaleCorrections = False

if doPhotonScaleCorrections:
    photonAna.doPhotonScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',
    'isSync': False
    }


isoTrackAna.setOff = False
genAna.allGenTaus  = True

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
#                        ttHFatJetAna)
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

# Tree Producer
from CMGTools.StopsDilepton.treeProducerStopsDilepton import *

if storePackedCandidates:
    from CMGTools.TTHAnalysis.analyzers.packedCandidateAnalyzer import packedCandidateAnalyzer
    packedCandidateAna = cfg.Analyzer(
        packedCandidateAnalyzer, name = 'packedCandidateAnalyzer',
        packedCandidates = 'packedPFCandidates',
    )
    susyCoreSequence.append( packedCandidateAna )

    susySingleLepton_collections.update( { "packedCandidates" : NTupleCollection("pf",     particleType, 15000, help="packed candidates (pf)")} )


from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer 
LHEAna = LHEAnalyzer.defaultConfig

#lheWeightAna.useLumiInfo=True

from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *

#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v121
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v175
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v220
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v278
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v285

triggerFlagsAna.triggerBits = {
    'mu'           : ["HLT_IsoMu27_v*", "HLT_IsoMu30_v*"],
    'mu_pre'       : ["HLT_IsoMu24_v*", "HLT_IsoMu24_eta2p1_v*", "HLT_Mu8_TrkIsoVVL_v*", "HLT_Mu8_v*", "HLT_Mu3_PFJet40_v*"],
    'mu_nonIso'    : ["HLT_Mu50_v*", "HLT_Mu55_v*"],
    'mu_nonIso_pre': ["HLT_Mu17_v*", "HLT_Mu19_v*", "HLT_Mu20_v*", "HLT_Mu27_v*"],

    'ele'          : ["HLT_Ele32_WPTight_Gsf_v*", "HLT_Ele35_WPTight_Gsf_v*", "HLT_Ele38_WPTight_Gsf_v*", "HLT_Ele40_WPTight_Gsf_v*"],
    'ele_pre'      : ["HLT_Ele27_WPTight_Gsf_v*", "HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*", "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*"],

    'mumu'         : ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*", "HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v*"],
    'mumu_pre'     : ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*"],
    'mumu_ht'      : ["HLT_DoubleMu4_Mass8_DZ_PFHT350_v*"],

    "mue"          : ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*", "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*" ],
    "mue_pre"      : ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*"], 
    "mue_ht"       : ["HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v*"],

    "ee"           : ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*" ],
    "ee_ht"        : ["HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v*"], 

    "mmm"          : ["HLT_TripleMu_10_5_5_DZ_v*", "HLT_TripleMu_5_3_3_Mass3p8to60_DZ_v*", "HLT_TripleMu_12_10_5_v*" ],
    "mme"          : ["HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v*", "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v*" ],
    "mee"          : ["HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v*", "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v*" ],
    "eee"          : ["HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v*" ],

    "IsoMu27"      : [ "HLT_IsoMu27_v*" ],
    "IsoMu30"      : [ "HLT_IsoMu30_v*" ],
    "IsoMu24"      : [ "HLT_IsoMu24_v*" ],
    "IsoMu24_eta2p1":[ "HLT_IsoMu24_eta2p1_v*" ],
    "Mu8_TrkIsoVVL": [ "HLT_Mu8_TrkIsoVVL_v*" ],
    "Mu8"          : [ "HLT_Mu8_v*" ],
    "Mu3_PFJet40"  : [ "HLT_Mu3_PFJet40_v*"],
    "Mu50"         : [ "HLT_Mu50_v*" ],
    "Mu55"         : [ "HLT_Mu55_v*" ],
    "Mu17"         : [ "HLT_Mu17_v*" ],
    "Mu19"         : [ "HLT_Mu19_v*" ],
    "Mu20"         : [ "HLT_Mu20_v*" ],
    "Mu27"         : [ "HLT_Mu27_v*" ],

    "Ele32_WPTight_Gsf"   : [ "HLT_Ele32_WPTight_Gsf_v*" ],
    "Ele35_WPTight_Gsf"   : [ "HLT_Ele35_WPTight_Gsf_v*" ],
    "Ele38_WPTight_Gsf"   : [ "HLT_Ele38_WPTight_Gsf_v*" ],
    "Ele40_WPTight_Gsf"   : [ "HLT_Ele40_WPTight_Gsf_v*" ],
    "Ele27_WPTight_Gsf"   : [ "HLT_Ele27_WPTight_Gsf_v*" ],
    "Ele17_CaloIdM_TrackIdM_PFJet30"   : [ "HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*" ],
    "Ele8_CaloIdM_TrackIdM_PFJet30"    : [ "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*" ],

    "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8"     : [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*" ],
    "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8"   : [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*" ],
    "Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8"   : [ "HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v*" ],
    "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL"              : [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*" ],
    "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ"           : [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*" ],
    "DoubleMu4_Mass8_DZ_PFHT350"                : [ "HLT_DoubleMu4_Mass8_DZ_PFHT350_v*" ],

    "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL"   : [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*" ],
    "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ": [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*" ],
    "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ" : [ "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*" ], 
    "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL"    : [ "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*" ],
    "Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ"    : [ "HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v*" ],

    "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL"             : [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*" ],
    "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"          : [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*" ], 
    "DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350"   : [ "HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v*" ],

    "TripleMu_10_5_5_DZ"                : [ "HLT_TripleMu_10_5_5_DZ_v*" ],
    "TripleMu_5_3_3_Mass3p8to60_DZ"     : [ "HLT_TripleMu_5_3_3_Mass3p8to60_DZ_v*" ],
    "TripleMu_12_10_5"                  : [ "HLT_TripleMu_12_10_5_v*" ], 
    "DiMu9_Ele9_CaloIdL_TrackIdL"       : [ "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v*" ],
    "DiMu9_Ele9_CaloIdL_TrackIdL_DZ"    : [ "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v*" ], 
    "Mu8_DiEle12_CaloIdL_TrackIdL"      : [ "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v*" ],
    "Mu8_DiEle12_CaloIdL_TrackIdL_DZ"   : [ "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v*" ], 
    "Ele16_Ele12_Ele8_CaloIdL_TrackIdL" : [ "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v*" ], 

}

trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    #trgObjSelectors = [ lambda t : t.path("HLT_IsoMu22_v*",1,0) or t.path("HLT_IsoMu20_v*",1,0) ],
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu27_v*",1,0) or t.path("HLT_IsoMu30_v*",1,0) ],#"HLT_IsoMu22", "HLT_IsoTkMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22_eta2p1", "HLT_IsoMu24", "HLT_IsoTkMu24"
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.3,
    univoqueMatching = True,
    verbose = False,
)
trigMatcher1El = trigMatcher1Mu.clone(
    name="trigMatcher1El",
    label='1El',
    #trgObjSelectors = [ lambda t : t.path("HLT_Ele27_eta2p1_WP75_Gsf_v*",1,0) or t.path("HLT_Ele27_eta2p1_WPLoose_Gsf_v*",1,0) ],
    #"HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"
    trgObjSelectors = [ lambda t : t.path("HLT_Ele32_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele35_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele38_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele40_WPTight_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1Mu)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1El)

# puppiMET
metPuppiAna = cfg.Analyzer(
    METAnalyzer, name="metPuppiAnalyzer",
    metCollection     = "slimmedMETsPuppi",
    noPUMetCollection = "slimmedMETsPuppi",
    copyMETsByValue = False,
    doTkMet = False,
    includeTkMetCHS = False,
    includeTkMetPVLoose = False,
    includeTkMetPVTight = False,
    doMetNoPU = False,
    doMetNoMu = False,
    doMetNoEle = False,
    doMetNoPhoton = False,
    recalibrate = False,
    applyJetSmearing = False, # does nothing unless the jet smearing is turned on in the jet analyzer
    old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
    jetAnalyzerCalibrationPostFix = "",
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    collectionPostFix = "Puppi",
    storePuppiExtra = False,
    )

## Tree Producer
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

#!# #-------- SAMPLES AND SEQUENCE -----------

selectedComponents = [
        ]

sequence = cfg.Sequence(
  susyCoreSequence+
      [ 
        LHEAna,
        metPuppiAna,
        ttHEventAna,
        treeProducer,
        ])

#if True or getHeppyOption("loadSamples"):
if getHeppyOption("loadSamples"):
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIISummer17MiniAODv2 import *
    for sample in dataSamples:
        #sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt"
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
    
    #selectedComponents = [TT_pow]
    #selectedComponents = [SingleMuon_Run2017D]
    selectedComponents = [SingleMuon_Run2017F]
    for comp in selectedComponents:
            comp.files = comp.files[:1]
            #comp.files = []
            #for i in range(41):
            #    if i == 39: continue #missing file
            #    fn = 'event_%s.root'%i
            #    comp.files.append(fn)
            #comp.files = ['root://eoscms.cern.ch//store/data/Run2017D/SingleMuon/MINIAOD/PromptReco-v1/000/302/031/00000/268C0C2A-498F-E711-872D-02163E019DAB.root']
            #comp.files = ['root://eoscms.cern.ch//store/group/phys_jetmet/MetScanners/bobak_pickevents_miniAOD.root']
            #comp.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/110000/16AAAA26-1F8E-E711-8B55-44A842CFC98B.root']
            comp.files = ['root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleMuon/MINIAOD/PromptReco-v1/000/306/134/00000/1E8CC801-C2C6-E711-8397-FA163E158EBC.root']
            comp.splitFactor = 1

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

#preprocessorFile = "$CMSSW_BASE/python/CMGTools/StopsDilepton/preprocessor/runBTaggingSlimPreprocessor_cfg.py"
#from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
#preprocessor = CmsswPreprocessor(preprocessorFile)
#jetAna.jetCol = 'selectedUpdatedPatJets'

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     # preprocessor=preprocessor, # comment if pre-processor non needed
                     events_class = event_class)

