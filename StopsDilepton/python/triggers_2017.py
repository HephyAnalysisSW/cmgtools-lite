from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *

#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v121
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v175
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v220
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v278
#https://cmswbm.cern.ch/cmsdb/servlet/TriggerMode?KEY=l1_hlt_collisions2017/v285

triggerBits = {
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
