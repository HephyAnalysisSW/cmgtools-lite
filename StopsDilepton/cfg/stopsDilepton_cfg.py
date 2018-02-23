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
lheWeightAna.usePSweights = True

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

    "IsoMu24"      : [ "HLT_IsoMu24_v*" ],
    "IsoMu27"      : [ "HLT_IsoMu27_v*" ],
    "IsoMu30"      : [ "HLT_IsoMu30_v*" ],
    "IsoMu24_eta2p1":[ "HLT_IsoMu24_eta2p1_v*" ],
    "Mu8_TrkIsoVVL": [ "HLT_Mu8_TrkIsoVVL_v*" ],
    "Mu8"          : [ "HLT_Mu8_v*" ],
    "Mu3_PFJet40"  : [ "HLT_Mu3_PFJet40_v*"],
    "Mu17"         : [ "HLT_Mu17_v*" ],
    "Mu19"         : [ "HLT_Mu19_v*" ],
    "Mu20"         : [ "HLT_Mu20_v*" ],
    "Mu24"         : [ "HLT_Mu24_v*" ],
    "Mu27"         : [ "HLT_Mu27_v*" ],
    "Mu50"         : [ "HLT_Mu50_v*" ],
    "Mu55"         : [ "HLT_Mu55_v*" ],

    "Ele27_WPTight_Gsf"   : [ "HLT_Ele27_WPTight_Gsf_v*" ],
    "Ele32_WPTight_Gsf"   : [ "HLT_Ele32_WPTight_Gsf_v*" ],
    "Ele35_WPTight_Gsf"   : [ "HLT_Ele35_WPTight_Gsf_v*" ],
    "Ele38_WPTight_Gsf"   : [ "HLT_Ele38_WPTight_Gsf_v*" ],
    "Ele40_WPTight_Gsf"   : [ "HLT_Ele40_WPTight_Gsf_v*" ],
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


    # MET triggers
    "MET_had": ['HLT_CaloMET100_HBHECleaned_v*', 'HLT_CaloMET100_NotCleaned_v*', 'HLT_CaloMET110_NotCleaned_v*', 'HLT_CaloMET250_HBHECleaned_v*', 'HLT_CaloMET250_NotCleaned_v*', 'HLT_CaloMET300_HBHECleaned_v*', 'HLT_CaloMET350_HBHECleaned_v*', 'HLT_CaloMET70_HBHECleaned_v*', 'HLT_CaloMET80_HBHECleaned_v*', 'HLT_CaloMET80_NotCleaned_v*', 'HLT_CaloMET90_HBHECleaned_v*', 'HLT_CaloMET90_NotCleaned_v*', 'HLT_CaloMHT90_v*', 'HLT_DiJet110_35_Mjj650_PFMET110_v*', 'HLT_DiJet110_35_Mjj650_PFMET120_v*', 'HLT_DiJet110_35_Mjj650_PFMET130_v*', 'HLT_L1ETMHadSeeds_v*', 'HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1_v*', 'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v*', 'HLT_PFMET110_PFMHT110_IDTight_CaloBTagCSV_3p1_v*', 'HLT_PFMET110_PFMHT110_IDTight_v*', 'HLT_PFMET120_PFMHT120_IDTight_CaloBTagCSV_3p1_v*', 'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v*', 'HLT_PFMET120_PFMHT120_IDTight_v*', 'HLT_PFMET130_PFMHT130_IDTight_CaloBTagCSV_3p1_v*', 'HLT_PFMET130_PFMHT130_IDTight_v*', 'HLT_PFMET140_PFMHT140_IDTight_CaloBTagCSV_3p1_v*', 'HLT_PFMET140_PFMHT140_IDTight_v*', 'HLT_PFMET200_HBHECleaned_v*', 'HLT_PFMET200_HBHE_BeamHaloCleaned_v*', 'HLT_PFMET200_NotCleaned_v*', 'HLT_PFMET250_HBHECleaned_v*', 'HLT_PFMET300_HBHECleaned_v*', 'HLT_PFMETTypeOne110_PFMHT110_IDTight_v*', 'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v*', 'HLT_PFMETTypeOne120_PFMHT120_IDTight_v*', 'HLT_PFMETTypeOne130_PFMHT130_IDTight_v*', 'HLT_PFMETTypeOne140_PFMHT140_IDTight_v*', 'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v*', 'HLT_TripleJet110_35_35_Mjj650_PFMET110_v*', 'HLT_TripleJet110_35_35_Mjj650_PFMET120_v*', 'HLT_TripleJet110_35_35_Mjj650_PFMET130_v*'],
    "MET_IsoTrk" :[ 'HLT_MET105_IsoTrk50_v*', 'HLT_MET120_IsoTrk50_v*', 'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v*'],
    "MET_PFMETNoMu":['HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v*', 'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v*', 'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v*', 'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v*', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v*', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v*', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*', 'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v*', 'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v*', 'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v*'],

    "HTMHT_had": ['HLT_PFHT500_PFMET100_PFMHT100_IDTight_v*', 'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v*', 'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v*', 'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v*', 'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v*', 'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v*', 'HLT_Rsq0p35_v*', 'HLT_Rsq0p40_v*', 'HLT_RsqMR300_Rsq0p09_MR200_4jet_v*', 'HLT_RsqMR300_Rsq0p09_MR200_v*', 'HLT_RsqMR320_Rsq0p09_MR200_4jet_v*', 'HLT_RsqMR320_Rsq0p09_MR200_v*'],

        # hadronic
        'HT350_MET100': triggers_HT350_MET100,
        "HT350":triggers_HT350,
        "HT475":triggers_HT475,
        "HT600":triggers_HT600,
        "dijet":triggers_dijet,
        "jet":triggers_jet,
        "dijet70met120": triggers_dijet70met120,
        "dijet55met110": triggers_dijet55met110,

        'HT900'                :triggers_HT900,
        'HT800'                :triggers_HT800,
        'MET170_NotCleaned'    :triggers_MET170_NotCleaned,
        'MET170_HBHECleaned'   :triggers_MET170_HBHECleaned,
        'MET170_BeamHaloCleaned':triggers_MET170_BeamHaloCleaned,
        'AllMET170'            :triggers_AllMET170,
        'AllMET300'            :triggers_AllMET300,
        'HT350_MET100'         :triggers_HT350_MET100,

#dilepton+HT
        'ee_ht':triggers_ee_ht,
        'mue_ht':triggers_mue_ht,
#fake rate
        'FR_1mu_iso':triggers_FR_1mu_iso,
        'FR_1mu_noiso':triggers_FR_1mu_noiso,
        'FR_1e_noiso':triggers_FR_1e_noiso,
        'FR_1e_iso':triggers_FR_1e_iso,
        'FR_1e_b2g':triggers_FR_1e_b2g,
#MET
        'Jet80MET90'       :triggers_Jet80MET90      ,
        'Jet80MET120'      :triggers_Jet80MET120     ,
        'MET120Mu5'        :triggers_MET120Mu5       ,
        'PFMET120_PFMHT120_IDTight':                    ['HLT_PFMET120_PFMHT120_IDTight_v*'],
        'PFMET120_PFMHT120_IDTight_PFHT60':             ['HLT_PFMET120_PFMHT120_IDTight_PFHT60_v*'],
        'PFMET130_PFMHT130_IDTight':                    ['HLT_PFMET130_PFMHT130_IDTight_v*'],
        'PFMET140_PFMHT140_IDTight':                    ['HLT_PFMET140_PFMHT140_IDTight_v*'],
        'PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60':     ['HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v*'],
        'PFMETNoMu120_PFMHTNoMu120_IDTight':            ['HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*'],

# individual triggers
        'Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ':            ['HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*'],
        'IsoMu22':                                      ['HLT_IsoMu22_v*'],
        'IsoTkMu22':                                    ['HLT_IsoTkMu22_v*'],
        'IsoMu22_eta2p1':                               ['HLT_IsoMu22_eta2p1_v*'],
        'IsoTkMu22_eta2p1':                             ['HLT_IsoTkMu22_eta2p1_v*'],
        'IsoTkMu24':                                    ['HLT_IsoTkMu24_v*'],
        'Ele25_eta2p1_WPTight_Gsf':                     ['HLT_Ele25_eta2p1_WPTight_Gsf_v*'],
        'Ele27_eta2p1_WPLoose_Gsf':                     ['HLT_Ele27_eta2p1_WPLoose_Gsf_v*'],
        'Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned':['HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v*'],
        'Ele28_eta2p1_WPTight_Gsf_HT150':               ['HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*'],
        'Ele32_WPTight_Gsf_L1DoubleEG':                 ['HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*'],
        'Ele115_CaloIdVT_GsfTrkIdT':                    ['HLT_Ele115_CaloIdVT_GsfTrkIdT_v*'],
        'Ele50_CaloIdVT_GsfTrkIdT_PFJet165':            ['HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v*'],
        'Photon175':                                    ['HLT_Photon175_v*'],
        'Photon200':                                    ['HLT_Photon200_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL':   ['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ':['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
}

trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    #trgObjSelectors = [ lambda t : t.path("HLT_IsoMu22_v*",1,0) or t.path("HLT_IsoMu20_v*",1,0) ],
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
    #trgObjSelectors = [ lambda t : t.path("HLT_Ele27_eta2p1_WP75_Gsf_v*",1,0) or t.path("HLT_Ele27_eta2p1_WPLoose_Gsf_v*",1,0) ],
    #"HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"
    trgObjSelectors = [ lambda t : t.path("HLT_Ele27_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele32_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele35_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele38_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele40_WPTight_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1Mu)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1El)

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
        ttHEventAna,
        treeProducer,
        ])

#if True or getHeppyOption("loadSamples"):
if getHeppyOption("loadSamples"):
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import *
    for sample in dataSamples:
        #sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt"
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
    
    selectedComponents = [T_sch_lep]
    #selectedComponents = [DoubleMuon_Run2017D_17Nov2017]
    #selectedComponents = [DYJetsToLL_M50_LO_ext]
    for comp in selectedComponents:
            comp.files = comp.files[:1]
            print comp.files
            #comp.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10_ext1-v2/10000/00F9D855-E293-E711-B625-02163E014200.root']
            #for i in range(41):
            #    if i == 39: continue #missing file
            #    fn = 'event_%s.root'%i
            #    comp.files.append(fn)
            #comp.files = ['root://eoscms.cern.ch//store/data/Run2017D/SingleMuon/MINIAOD/PromptReco-v1/000/302/031/00000/268C0C2A-498F-E711-872D-02163E019DAB.root']
            #comp.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3E1DE3B8-87C0-E611-8733-00145EDD74ED.root']
            #comp.files = ['root://eoscms.cern.ch//store/group/phys_jetmet/MetScanners/bobak_pickevents_miniAOD.root']
            #comp.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/110000/16AAAA26-1F8E-E711-8B55-44A842CFC98B.root']
            #comp.files = ['root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleMuon/MINIAOD/PromptReco-v1/000/306/134/00000/1E8CC801-C2C6-E711-8397-FA163E158EBC.root']
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

