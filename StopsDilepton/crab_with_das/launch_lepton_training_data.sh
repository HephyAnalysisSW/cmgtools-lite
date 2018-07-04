#!/bin/sh

##QCD

#QCDPtEMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_EMEnriched_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_EMEnriched
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300toInf_EMEnriched

#QCDPtbcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_20to30_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_30to80_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_80to170_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_170to250_bcToE
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt_250toInf_bcToE

#QCD_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt15to20_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt600to800_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt600to800_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5_ext2
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt1000toInf_Mu5
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt1000toInf_Mu5_ext


##TTJets

#TTJetsSingleLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromTbar
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromTbar_ext
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromT
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromT_ext

#TTJetsDiLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_DiLepton
python launch.py --year=2016 --remoteDir="lepton" --unitsPerJob=3 --production_label="lepton_v1" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_DiLepton_ext


#make this file executable: chmod +x launch_lepton_training_data.sh
#execute this file in shell: ./launch_lepton_training_data.sh
#samplelist: CMGTools/RootTools/python/samples/samples_13TeV_RunIISummer16MiniAODv2.py
#display status: for x in `ls crab_*/* -d`; do crab status $x; done
#see also Dashboard monitoring URL
#data saved in: dpns-ls -l /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton

#root: dpns-ls /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root 
#root: root -b root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root
