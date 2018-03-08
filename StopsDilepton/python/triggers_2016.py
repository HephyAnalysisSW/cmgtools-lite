from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *
triggerBits = {
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

        ## muon

        'SingleMu_iso'     :triggers_1mu_iso,
        'SingleMu_noniso'  :triggers_1mu_noniso ,
        'SingleMuTTZ'      :triggers_1mu_iso_TTZ,

        'SingleEle_noniso'   :triggers_1e_noniso,
        'SingleEle'          :triggers_1e,
        'SingleEleTTZ'       :triggers_1e_iso_TTZ,

#mumu
        'mumuIso' : triggers_mumu_iso,
        'mumuNoiso' : triggers_mumu_noniso,
        'mumuSS' : triggers_mumu_ss,
        'mumuHT' : triggers_mumu_ht,
# ee
        'ee_DZ': triggers_ee,
        'ee_noDZ':triggers_ee_nodz ,
        'ee_noniso':triggers_ee_noniso,
        'ee_33': ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*'],
        'ee_33_MW': ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v*'],
        'eeSS' : triggers_ee_ss,
#mue
        'mue':triggers_mue,
        'mu30e30': ['HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v*'],
#dilepton+HT
        'ee_ht':triggers_ee_ht,
        'mue_ht':triggers_mue_ht,
#multi-lepton
        '3e':triggers_3e,
        '3mu':triggers_3mu,
        '3mu_alt':triggers_3mu_alt,
        '2mu1e':triggers_2mu1e,
        '2e1mu':triggers_2e1mu,
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

        'DoubleMu3_PFMET50' : ['HLT_DoubleMu3_PFMET50_v*'],
        'Mu6_PFHT200_PFMET100' : ['HLT_Mu6_PFHT200_PFMET100_v*'],
        'PFMET110_PFMHT110_IDTight': ['HLT_PFMET110_PFMHT110_IDTight_v*'], #prescaled
        'PFMET120_PFMHT120_IDTight': ['HLT_PFMET120_PFMHT120_IDTight_v*'],

        "MET_had": [ "HLT_MET200_v*", "HLT_MET250_v*", "HLT_MET300_v*", "HLT_PFMET100_PFMHT100_IDTight_v*", "HLT_PFMET110_PFMHT110_IDTight_v*", "HLT_PFMET120_BTagCSV0p72_v*", "HLT_PFMET120_PFMHT120_IDTight_v*", "HLT_PFMET170_HBHECleaned_v*", "HLT_PFMET170_JetIdCleaned_v*", "HLT_PFMET170_NoiseCleaned_v*", "HLT_PFMET170_v*", "HLT_PFMET300_v*", "HLT_PFMET400_v*", "HLT_PFMET90_PFMHT90_IDTight_v*", "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v*", "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v*", "HLT_QuadPFJet_VBF_v*"],
        "MET_IsoTrk":[ "HLT_MET60_IsoTrk35_Loose_v*", "HLT_MET75_IsoTrk50_v*", "HLT_MET90_IsoTrk50_v*"], 
        "MET_PFMETNoMu": ["HLT_MonoCentralPFJet80_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
        "MET_PFMETNoMu_JetIdCleaned":[ "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*", "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*", "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*", "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
        "MET_MuXer": ["HLT_Mu14er_PFMET100_v*", "HLT_Mu3er_PFHT140_PFMET125_v*", "HLT_Mu6_PFHT200_PFMET100_v*", "HLT_Mu6_PFHT200_PFMET80_BTagCSV0p72_v*", "HLT_PFMET120_Mu5_v*"],

        "HTMHT_had": [ "HLT_DiCentralPFJet55_PFMET110_v*", "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v*", "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v*", "HLT_PFHT200_PFAlphaT0p51_v*", "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v*", "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v*", "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v*", "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v*", "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v*", "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v*", "HLT_PFHT350_PFMET100_v*", "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v*", "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v*", "HLT_Rsq0p25_v*", "HLT_Rsq0p30_v*", "HLT_RsqMR240_Rsq0p09_MR200_4jet_v*", "HLT_RsqMR240_Rsq0p09_MR200_v*", "HLT_RsqMR270_Rsq0p09_MR200_4jet_v*", "HLT_RsqMR270_Rsq0p09_MR200_v*"],
        "HTMHT_PFMETNoMu":[ "HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v*", "HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v*"],

# individual triggers
        'Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*'],
        'Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ': ['HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*'],
        'IsoMu22': ['HLT_IsoMu22_v*'],
        'IsoTkMu22': ['HLT_IsoTkMu22_v*'],
        'IsoMu22_eta2p1': ['HLT_IsoMu22_eta2p1_v*'],
        'IsoTkMu22_eta2p1': ['HLT_IsoTkMu22_eta2p1_v*'],
        'IsoMu24': ['HLT_IsoMu24_v*'],
        'IsoTkMu24': ['HLT_IsoTkMu24_v*'],
        'Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'Ele27_WPTight_Gsf': ['HLT_Ele27_WPTight_Gsf_v*'],
        'Ele25_eta2p1_WPTight_Gsf': ['HLT_Ele25_eta2p1_WPTight_Gsf_v*'],
        'Ele27_eta2p1_WPLoose_Gsf': ['HLT_Ele27_eta2p1_WPLoose_Gsf_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL': ['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL': ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*'],
        'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'DiMu9_Ele9_CaloIdL_TrackIdL': ['HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v*'],
        'Mu8_DiEle12_CaloIdL_TrackIdL': ['HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v*'],
        'TripleMu_12_10_5': ['HLT_TripleMu_12_10_5_v*'],
        'Ele16_Ele12_Ele8_CaloIdL_TrackIdL': ['HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v*'],
}
