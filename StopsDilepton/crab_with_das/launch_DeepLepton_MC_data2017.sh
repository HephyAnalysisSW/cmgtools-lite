#!/bin/sh

##QCD

#QCDPtEMEnriched
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt15to20_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_EMEnriched 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300toInf_EMEnriched
 
#QCDPtbcToE
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt15to20_bcToE 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_bcToE 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to80_bcToE 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to170_bcToE 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to250_bcToE 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt250toInf_bcToE 

#QCD_Mu5
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt15to20_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt20to30_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt30to50_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt50to80_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt80to120_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt120to170_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt170to300_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt300to470_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt470to600_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt600to800_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt800to1000_Mu5 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" QCD_Pt1000toInf_Mu5


##TTJets

#TTs
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTHad_pow 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTSemi_pow 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTJets_SingleLeptonFromT
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow_TuneDown 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow_TuneUp 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow_hdampDown 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" TTLep_pow_hdampUp


#Drell-Jan

#DYJets
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_ext 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_LO 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_LO_ext 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M10to50_LO

#DYNJetsToLL
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY1JetsToLL_M50_LO 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY1JetsToLL_M50_LO_ext 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY2JetsToLL_M50_LO 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY2JetsToLL_M50_LO_ext 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY3JetsToLL_M50_LO 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY3JetsToLL_M50_LO_ext 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DY4JetsToLL_M50_LO 

#DYJetsToLLM4to50HT
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT70to100 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT70to100_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT100to200 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT100to200_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT200to400 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT200to400_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT400to600 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT400to600_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M4to50_HT600toInf 

#DYJetsToLLM50HT
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT100to200 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT100to200_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT200to400 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT200to400_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT400to600 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT400to600_ext1 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT600to800 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT800to1200 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT1200to2500 
python launch.py --year=2017 --remoteDir="lepton" --unitsPerJob=2 --production_label="lepton2017_v2" --cfg_name "../cfg/lepton_%i_cfg.py" DYJetsToLL_M50_HT2500toInf 


#make this file executable: chmod +x launch_lepton_training_data.sh
#execute this file in shell: ./launch_lepton_training_data.sh
#samplelist: CMGTools/RootTools/python/samples/samples_13TeV_RunIISummer16MiniAODv2.py
#display status: for x in `ls crab_*/* -d`; do crab status $x; done #see also Dashboard monitoring URL
#data saved in: dpns-ls -l /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton

#root: dpns-ls /dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root 
#root: root -b root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/gmortl/cmgTuples/lepton/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_lepton_v1/180621_115116/0000/tree_9.root
