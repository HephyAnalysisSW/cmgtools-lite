#!/bin/sh

##QCD

#QCDPtEMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300toInf_EMEnriched

#QCDPtbcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_20to30_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_30to80_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_80to170_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_170to250_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_250toInf_bcToE

#QCD_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt15to20_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt600to800_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt600to800_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt1000toInf_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt1000toInf_Mu5_ext


##TTJets

#TTJetsSingleLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromTbar
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromTbar_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromT
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromT_ext

#TTJetsDiLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_DiLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_DiLepton_ext

##TTJets others
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_LO
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TT_pow_ext3
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TT_pow
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTSemiLep_pow
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_LO_HT600to800_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_LO_HT800to1200_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_LO_HT1200to2500_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_LO_HT2500toInf_ext


#Drell-Jan

#VJets
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M10to50
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M10to50_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M10to50_LO
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_LO_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_LO_ext2

#DYNJets
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY1JetsToLL_M50_LO
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY2JetsToLL_M50_LO
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY3JetsToLL_M50_LO
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY4JetsToLL_M50_LO

#DYJetsM50HT
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT70to100
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT100to200
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT100to200_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT200to400
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT200to400_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT400to600
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT400to600_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT600toInf
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT600toInf_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT600to800
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT800to1200
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT1200to2500
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT2500toInf

#DYJetsM5to50HT
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT70to100
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT100to200
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT100to200_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT200to400
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT200to400_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT400to600
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT400to600_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT600toInf
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M5to50_HT600toInf_ext


#make this file executable: chmod +x launch_lepton_training_data.sh
#execute this file in shell: ./launch_lepton_training_data.sh
#samplelist: CMGTools/RootTools/python/samples/samples_13TeV_RunIISummer16MiniAODv2.py
#display status: for x in `ls crab_*/* -d`; do crab status $x; done
#see also Dashboard monitoring URL
#data saved in: dpns-ls -l /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton

#root: dpns-ls /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root 
#root: root -b root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root
