PROD_LABEL="8025_mAODv2_v10"
REMOTE_DIR_DATA="${PROD_LABEL}/Data25ns"
REMOTE_DIR_MC="${PROD_LABEL}/RunIISummer16MiniAODv2"
#REMOTE_DIR_MC="${PROD_LABEL}/RunIISpring16MiniAODv2"

echo --------------------------------------------
echo 
echo $PROD_LABEL
echo $REMOTE_DIR_DATA
echo $REMOTE_DIR_MC
echo
echo --------------------------------------------

test=false
data=false
w=false
tt=false
z=false
qcd=false
sig=false
bmsig=false
dy=false
qcdpt=false
vv=false
st=false
ttx=false
sigfullsim=false
ewikino=false


for i in "$@"
do
case $i in
    test)
    test=true
    testtag=$2
    echo Will Only Run a Test Job  $test $testtag
    shift
    ;;

    sig)
    sig=true
    echo Will Process Priv Signals:  $sig 
    shift
    ;;

    bmsig)
    bmsig=true
    echo Will Process Priv Signals:  $bmsig 
    shift
    ;;
    sigfullsim)
    sigfullsim=true
    echo Will Process Official Signals:  $sigfullsim 
    shift
    ;;

    ewikino)
    ewikino=true
    echo Will Process Official Signals:  $ewikino 
    shift
    ;;

    data)
    data=true
    echo Will Process Data:  $data 
    shift
    ;;

    w)
    w=true
    echo Will Process WJets:  $w
    shift
    ;;

    tt)
    tt=true
    echo Will Process TTJets:  $tt
    shift
    ;;

    qcd)
    qcd=true
    echo Will Process QCD:  $qcd
    shift
    ;;

    z)
    z=true
    echo Will Process ZJets:  $z
    shift
    ;;

    dy)
    dy=true
    echo Will Process DYJets:  $dy
    shift
    ;;

    st)
    st=true
    echo Will Process Single Tops:  $st 
    shift
    ;;

    qcdpt)
    qcdpt=true
    echo Will Process QCD pt:  $qcdpt 
    shift
    ;;

    vv)
    vv=true
    echo Will Process VV:  $vv 
    shift
    ;;

    ttx)
    ttx=true
    echo Will Process ttX:  $ttx
    shift
    ;;

    all)
    vv=true
    qcd=true
    dy=true
    z=true
    tt=true
    w=true
    data=true
    st=true
    ttx=true
    #sig=true
    #sigfullsim=true
    echo Will Process everything! 
    shift
    ;;
esac
done

if $test
  then
  echo "ONLY TESTING"
  python launch.py --unitsPerJob=50 --remoteDir="TEST_${testtag}/RunIISummer16MiniAODv2" --production_label="TEST_${testtag}"    TT_pow
  echo exit
  exit
fi

if $data
then
  #python launch.py --unitsPerJob=1 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL       MET_Run2015D_v4  MET_Run2015D_05Oct SingleMuon_Run2015D_v4  SingleMuon_Run2015D_05Oct SingleElectron_Run2015D_05Oct  SingleElectron_Run2015D_v4  
  echo ----------------------  Submitting DATA  ------ -----------------
  python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      MET_Run2016B_23Sep2016            MET_Run2016C_23Sep2016            MET_Run2016D_23Sep2016            MET_Run2016E_23Sep2016             MET_Run2016F_23Sep2016              MET_Run2016G_23Sep2016                 MET_Run2016H_PromptReco_v2              MET_Run2016H_PromptReco_v3                
  python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      JetHT_Run2016B_23Sep2016          JetHT_Run2016C_23Sep2016          JetHT_Run2016D_23Sep2016          JetHT_Run2016E_23Sep2016           JetHT_Run2016F_23Sep2016            JetHT_Run2016G_23Sep2016               JetHT_Run2016H_PromptReco_v2            JetHT_Run2016H_PromptReco_v3           
  python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleElectron_Run2016B_23Sep2016 SingleElectron_Run2016C_23Sep2016 SingleElectron_Run2016D_23Sep2016 SingleElectron_Run2016E_23Sep2016  SingleElectron_Run2016F_23Sep2016   SingleElectron_Run2016G_23Sep2016      SingleElectron_Run2016H_PromptReco_v2   SingleElectron_Run2016H_PromptReco_v3       
  python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleMuon_Run2016B_23Sep2016     SingleMuon_Run2016C_23Sep2016     SingleMuon_Run2016D_23Sep2016     SingleMuon_Run2016E_23Sep2016      SingleMuon_Run2016F_23Sep2016       SingleMuon_Run2016G_23Sep2016          SingleMuon_Run2016H_PromptReco_v2       SingleMuon_Run2016H_PromptReco_v3         
 
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL  MET_Run2016B_03Feb2017_v2  MET_Run2016C_03Feb2017  MET_Run2016D_03Feb2017  MET_Run2016E_03Feb2017  MET_Run2016F_03Feb2017  MET_Run2016G_03Feb2017  MET_Run2016H_03Feb2017_v2  MET_Run2016H_03Feb2017_v3
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL  JetHT_Run2016B_03Feb2017_v2  JetHT_Run2016C_03Feb2017  JetHT_Run2016D_03Feb2017  JetHT_Run2016E_03Feb2017  JetHT_Run2016F_03Feb2017  JetHT_Run2016G_03Feb2017  JetHT_Run2016H_03Feb2017_v2  JetHT_Run2016H_03Feb2017_v3
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL  SingleElectron_Run2016B_03Feb2017_v2  SingleElectron_Run2016C_03Feb2017  SingleElectron_Run2016D_03Feb2017  SingleElectron_Run2016E_03Feb2017  SingleElectron_Run2016F_03Feb2017  SingleElectron_Run2016G_03Feb2017  SingleElectron_Run2016H_03Feb2017_v2  SingleElectron_Run2016H_03Feb2017_v3
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL  SingleMuon_Run2016B_03Feb2017_v2  SingleMuon_Run2016C_03Feb2017  SingleMuon_Run2016D_03Feb2017  SingleMuon_Run2016E_03Feb2017  SingleMuon_Run2016F_03Feb2017  SingleMuon_Run2016G_03Feb2017  SingleMuon_Run2016H_03Feb2017_v2  SingleMuon_Run2016H_03Feb2017_v3
fi

if  $tt
then
  echo ----------------------  Submitting TTJets  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL TTJets_SingleLeptonFromTbar  TTJets_SingleLeptonFromTbar_ext  TTJets_SingleLeptonFromT  TTJets_SingleLeptonFromT_ext  TTJets_DiLepton  TTJets_DiLepton_ext  
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL TT_pow TT_pow_backup  
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL TTJets
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL TTJets_LO_HT600to800_ext  TTJets_LO_HT800to1200_ext  TTJets_LO_HT1200to2500_ext  TTJets_LO_HT2500toInf_ext
fi

if  $w
then
  echo ----------------------  Submitting WJets  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WJetsToLNu_HT70to100  WJetsToLNu_HT100to200  WJetsToLNu_HT100to200_ext  WJetsToLNu_HT100to200_ext2  WJetsToLNu_HT200to400  WJetsToLNu_HT200to400_ext2  WJetsToLNu_HT200to400_ext  WJetsToLNu_HT400to600  WJetsToLNu_HT400to600_ext  WJetsToLNu_HT600to800  WJetsToLNu_HT600to800_ext  WJetsToLNu_HT800to1200  WJetsToLNu_HT800to1200_ext  WJetsToLNu_HT1200to2500  WJetsToLNu_HT1200to2500_ext  WJetsToLNu_HT2500toInf  WJetsToLNu_HT2500toInf_ext
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WJetsToLNu WJetsToLNu_LO
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WJetsToLNu_Pt_100to250     WJetsToLNu_Pt_100to250_ext     WJetsToLNu_Pt_250to400     WJetsToLNu_Pt_250to400_ext     WJetsToLNu_Pt_400to600     WJetsToLNu_Pt_400to600_ext     WJetsToLNu_Pt_600toInf     WJetsToLNu_Pt_600toInf_ext
fi

if  $z
then
  echo ----------------------  Submitting ZJets  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL    ZJetsToNuNu_HT100to200  ZJetsToNuNu_HT100to200_ext  ZJetsToNuNu_HT200to400  ZJetsToNuNu_HT200to400_ext  ZJetsToNuNu_HT400to600  ZJetsToNuNu_HT400to600_ext  ZJetsToNuNu_HT600to800  ZJetsToNuNu_HT800to1200  ZJetsToNuNu_HT800to1200ext  ZJetsToNuNu_HT1200to2500  ZJetsToNuNu_HT1200to2500_ext  ZJetsToNuNu_HT2500toInf  ZJetsToNuNu_HT2500toInf_ext  
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL    ZJetsToNuNu_HT100to200  ZJetsToNuNu_HT100to200_ext  ZJetsToNuNu_HT200to400  ZJetsToNuNu_HT200to400_ext  ZJetsToNuNu_HT400to600  ZJetsToNuNu_HT400to600_ext  ZJetsToNuNu_HT600to800  ZJetsToNuNu_HT800to1200  ZJetsToNuNu_HT1200to2500  ZJetsToNuNu_HT1200to2500_ext  ZJetsToNuNu_HT2500toInf  
fi

if  $dy
then
  echo ----------------------  Submitting DY  -----------------------

  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   DYJetsToLL_M50_HT70to100     DYJetsToLL_M50_HT100to200  DYJetsToLL_M50_HT100to200_ext  DYJetsToLL_M50_HT200to400  DYJetsToLL_M50_HT200to400_ext  DYJetsToLL_M50_HT400to600  DYJetsToLL_M50_HT400to600_ext  DYJetsToLL_M50_HT600to800    DYJetsToLL_M50_HT800to1200   DYJetsToLL_M50_HT1200to2500  DYJetsToLL_M50_HT2500toInf   
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   DYJetsToLL_M5to50_HT100to200  DYJetsToLL_M5to50_HT100to200_ext  DYJetsToLL_M5to50_HT200to400  DYJetsToLL_M5to50_HT200to400_ext  DYJetsToLL_M5to50_HT400to600  DYJetsToLL_M5to50_HT400to600_ext  DYJetsToLL_M5to50_HT600toInf  DYJetsToLL_M5to50_HT600toInf_ext
fi

if  $qcd
then
  echo ----------------------  Submitting QCD  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   QCD_HT50to100  QCD_HT100to200  QCD_HT200to300  QCD_HT200to300_ext  QCD_HT300to500  QCD_HT300to500_ext  QCD_HT500to700  QCD_HT500to700_ext  QCD_HT700to1000  QCD_HT700to1000_ext  QCD_HT1000to1500  QCD_HT1000to1500_ext  QCD_HT1500to2000  QCD_HT1500to2000_ext  QCD_HT2000toInf  QCD_HT2000toInf_ext
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   QCD_HT100to200    QCD_HT200to300    QCD_HT200to300_ext    QCD_HT300to500    QCD_HT300to500_ext    QCD_HT500to700    QCD_HT500to700_ext    QCD_HT700to1000    QCD_HT700to1000_ext    QCD_HT1000to1500    QCD_HT1000to1500_ext    QCD_HT1500to2000    QCD_HT1500to2000_ext    QCD_HT2000toInf    QCD_HT2000toInf_ext
fi

if  $qcdpt
then
  echo ----------------------  Submitting pt-binned QCD  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  QCD_Pt15to20_Mu5   QCD_Pt20to30_Mu5   QCD_Pt30to50_Mu5   QCD_Pt50to80_Mu5   QCD_Pt80to120_Mu5   QCD_Pt80to120_Mu5_ext   QCD_Pt120to170_Mu5   QCD_Pt170to300_Mu5   QCD_Pt170to300_Mu5_ext   QCD_Pt300to470_Mu5   QCD_Pt300to470_Mu5_ext   QCD_Pt300to470_Mu5_ext2   QCD_Pt470to600_Mu5   QCD_Pt470to600_Mu5_ext   QCD_Pt470to600_Mu5_ext2   QCD_Pt600to800_Mu5   QCD_Pt600to800_Mu5_ext   QCD_Pt800to1000_Mu5   QCD_Pt800to1000_Mu5_ext   QCD_Pt800to1000_Mu5_ext2   QCD_Pt1000toInf_Mu5   QCD_Pt1000toInf_Mu5_ext
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  QCD_Pt20to30_EMEnriched   QCD_Pt30to50_EMEnriched   QCD_Pt30to50_EMEnriched_ext   QCD_Pt50to80_EMEnriched_ext   QCD_Pt80to120_EMEnriched_ext   QCD_Pt120to170_EMEnriched   QCD_Pt170to300_EMEnriched   QCD_Pt300toInf_EMEnriched
fi

if  $st
then
  echo ----------------------  Submitting Single Tops  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  T_tWch_ext  TBar_tWch_ext  T_tch_powheg TBar_tch_powheg
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  T_tWch   TBar_tWch    T_tch  TBar_tch  TToLeptons_tch_powheg TBarToLeptons_tch_powheg TToLeptons_sch_amcatnlo
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  T_tWch   TBar_tWch    T_tch  TBar_tch  #TToLeptons_tch_powheg TBarToLeptons_tch_powheg TToLeptons_sch_amcatnlo
fi

if  $vv
then
  echo ----------------------  Submitting Dibosons  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WWTo2L2Nu  WWToLNuQQ  WWToLNuQQ_ext  WWTo1L1Nu2Q #NOTE: NLO (high stat) 
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   ZZTo2L2Nu  ZZTo2L2Q     ZZTo2Q2Nu  ZZTo4L #NOTE: NLO (high stat) 
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WZTo1L3Nu  WZTo1L1Nu2Q  WZTo2L2Q   WZTo3LNu   WZTo3LNu_amcatnlo #NOTE: NLO (high stat) 
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WGJets  WGToLNuG #NOTE: NLO (high stat) 
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   VVTo2L2Nu  VVTo2L2Nu_ext #NOTE: NLO (high stat) 
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL WZ ZZ WW #TBar_tWch  T_tWch #NOTE: LO (low stat) 
fi

if  $ttx
then
  echo ----------------------  Submitting TTX  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   TTW_LO  TTZ_LO  TTGJets
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   TTWToLNu_ext  TTWToLNu_ext2  TTWToQQ  TTZToQQ  TTZToLLNuNu_ext  TTZToLLNuNu_m1to10
fi

if  $bmsig
then
  echo ----------------------  Submitting Official Signals  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_TChiWZ_genHT_160_genMET_80_3p         
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_N2N1_higgsino_genHT_160_genMET_80_3p  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_N2C1_higgsino_genHT_160_genMET_80_3p  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_C1N1_higgsino_genHT_160_genMET_80_3p  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_C1C1_higgsino_genHT_160_genMET_80_3p  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   MSSM_higgsino_genHT_160_genMET_80_3p
fi

if  $sig
then
  echo ----------------------  Submitting Official Signals  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2tt_dM_10to80_genHT_160_genMET_80
fi

if  $sigfullsim
then
  echo ------------------------------- Signal Deg Stop -----------------
  python launch.py   --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2tt_genHT_160_genMET_80_mStop_275_mLSP_205  SMS_T2tt_genHT_160_genMET_80_mStop_350_mLSP_330   SMS_T2tt_genHT_160_genMET_80_mStop_400_mLSP_350
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL --inputDBS="phys03"    T2DegStop_300_290_FastSim   T2DegStop_300_240_FastSim   T2DegStop_300_270_FastSim  T2tt_300_270_FastSim   
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL --inputDBS="phys03"    T2DegStop_300_270
fi

if  $ewikino
then
  echo ------------------------------- Signal EWKino -----------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   MSSM_higgsino_genHT_160_genMET_80  SMS_TChiWZ_genHT_160_genMET_80
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_TChiWZ_ZToLL_mZMin_0p1 
fi

