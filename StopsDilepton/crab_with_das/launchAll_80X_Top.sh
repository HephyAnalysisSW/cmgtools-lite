#!/bin/sh

### Background MC ttZ 3l
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=2 --production_label="80X_2l_v9" TTZ_LO
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTZToLLNuNu_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WZTo3LNu_amcatnlo
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTWToLNu_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTWToLNu_ext2
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTHnobb_pow
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTHbb_ext3
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" tZq_ll_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTGJets
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTGJets_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" tWll
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTTT
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ZZTo4L
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WZZ
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WWZ
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ZZZ
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WGToLNuG
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ZGTo2LG_ext

## Background MC ttZ 4l
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTZToLLNuNu_m1to10 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M10to50_LO
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_LO_ext 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_LO
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WWW
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" GGHZZ4L
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" VHToNonbb
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" THQ
# not included yet: GluGluToContinToZZ Higgs samples

## Background MC ttW
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_DiLepton
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_DiLepton_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_SingleLeptonFromTbar
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_SingleLeptonFromTbar_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_SingleLeptonFromT 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTJets_SingleLeptonFromT_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WWDoubleTo2L
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" WpWpJJ
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TGJets
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TGJets_ext

## Our additional stuff
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" TTLep_pow
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT70to100
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT100to200
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT100to200_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT200to400
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT200to400_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT400to600
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT400to600_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT600to800
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT800to1200
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT1200to2500
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M50_HT2500toInf
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT100to200
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT100to200_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT200to400
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT200to400_ext
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT400to600
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT600toInf
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" DYJetsToLL_M5to50_HT600toInf_ext

### signal MC
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000

python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH 
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_0p050000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_0p100000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_0p200000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_0p300000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_m0p150000
python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=3 --production_label="80X_2l_v9" ewkDM_ttZ_ll_noH_DC2V_m0p250000


## 2016 Data
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016B_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016C_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016D_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016E_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016F_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016G_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016H_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleMuon_Run2016H_03Feb2017_v3

#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016B_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016C_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016D_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016E_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016F_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016G_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016H_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" SingleElectron_Run2016H_03Feb2017_v3

#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016B_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016C_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016D_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016E_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016F_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016G_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016H_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleMuon_Run2016H_03Feb2017_v3
#
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016B_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016C_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016D_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016E_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016F_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016G_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016H_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" DoubleEG_Run2016H_03Feb2017_v3
#
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016B_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016C_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016D_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016E_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016F_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016G_03Feb2017
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016H_03Feb2017_v2
#python launch.py --remoteDir="80X_2l_v9" --unitsPerJob=1 --production_label="80X_2l_v9" MuonEG_Run2016H_03Feb2017_v3
