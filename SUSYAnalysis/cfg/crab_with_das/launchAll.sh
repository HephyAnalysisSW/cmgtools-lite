#PROD_LABEL="8020_mAODv2_v0"  
PROD_LABEL="8020_mAODv2_v0"  
#PROD_LABEL="8020_mAODv2_OldJetClean_v2"  
REMOTE_DIR_DATA="${PROD_LABEL}/Data25ns"
REMOTE_DIR_MC="${PROD_LABEL}/RunIISpring16MiniAODv2"


echo --------------------------------------------
echo 
echo $PROD_LABEL
echo $REMOTE_DIR_DATA
echo $REMOTE_DIR_MC
echo
echo --------------------------------------------


data=false
w=false
tt=false
z=false
qcd=false
sig=false
dy=false
qcdpt=false
vv=false
st=false
ttx=false
degstop=false
ewikino=false


for i in "$@"
do
case $i in
    sig)
    sig=true
    echo Will Process Priv Signals:  $sig 
    shift
    ;;
    degstop)
    degstop=true
    echo Will Process Official Signals:  $degstop 
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
    #degstop=true
    echo Will Process everything! 
    shift
    ;;
esac
done





if $data
then
  #python launch.py --unitsPerJob=1 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL       MET_Run2015D_v4  MET_Run2015D_05Oct SingleMuon_Run2015D_v4  SingleMuon_Run2015D_05Oct SingleElectron_Run2015D_05Oct  SingleElectron_Run2015D_v4  
  echo ----------------------  Submitting DATA  ------ -----------------
  # fixed for 80x

  python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL       JetHT_Run2016E_23Sep2016

  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      JetHT_Run2016B_23Sep2016_v1  JetHT_Run2016B_23Sep2016_v3  JetHT_Run2016C_23Sep2016_v1  JetHT_Run2016D_23Sep2016_v1  JetHT_Run2016E_23Sep2016_v1  JetHT_Run2016F_23Sep2016_v1  JetHT_Run2016G_23Sep2016_v1  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      MET_Run2016B_23Sep2016_v2  MET_Run2016B_23Sep2016_v3  MET_Run2016C_23Sep2016_v1  MET_Run2016D_23Sep2016_v1  MET_Run2016E_23Sep2016_v1  MET_Run2016F_23Sep2016_v1  MET_Run2016G_23Sep2016_v1  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleElectron_Run2016B_23Sep2016_v2  SingleElectron_Run2016B_23Sep2016_v3  SingleElectron_Run2016C_23Sep2016_v1  SingleElectron_Run2016D_23Sep2016_v1  SingleElectron_Run2016E_23Sep2016_v1  SingleElectron_Run2016F_23Sep2016_v1  SingleElectron_Run2016G_23Sep2016_v1  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleMuon_Run2016B_23Sep2016_v1  SingleMuon_Run2016B_23Sep2016_v3  SingleMuon_Run2016C_23Sep2016_v1  SingleMuon_Run2016D_23Sep2016_v1  SingleMuon_Run2016E_23Sep2016_v1  SingleMuon_Run2016F_23Sep2016_v1  SingleMuon_Run2016G_23Sep2016_v1

  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      JetHT_Run2016H_PromptReco_v1  JetHT_Run2016H_PromptReco_v2  JetHT_Run2016H_PromptReco_v3  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      MET_Run2016H_PromptReco_v1  MET_Run2016H_PromptReco_v2  MET_Run2016H_PromptReco_v3  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleElectron_Run2016H_PromptReco_v1  SingleElectron_Run2016H_PromptReco_v2  SingleElectron_Run2016H_PromptReco_v3  
  #python launch.py --unitsPerJob=50 --remoteDir=$REMOTE_DIR_DATA --production_label=$PROD_LABEL      SingleMuon_Run2016H_PromptReco_v1  SingleMuon_Run2016H_PromptReco_v2  SingleMuon_Run2016H_PromptReco_v3 


fi

if  $tt
then
  echo ----------------------  Submitting TTJets  -----------------------
  ## still missing some for 80x
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   TTJets_FastSIM   
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL                   TTJets_LO

  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   TTJets_LO  TTJets_LO_HT600to800_ext  TTJets_LO_HT800to1200_ext   TTJets_LO_HT1200to2500_ext TTJets_LO_HT2500toInf  #  TTJets_LO_HT600to800  TTJets_LO_HT800to1200   TTJets_LO_HT1200to2500  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   TTJets_SingleLeptonFromT TTJets_SingleLeptonFromTbar TTJets_DiLepton    

fi

if  $w
then
  echo ----------------------  Submitting WJets  -----------------------
  # fixed for 80x
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WJetsToLNu WJetsToLNu_LO  WJetsToLNu_HT100to200  WJetsToLNu_HT100to200_ext WJetsToLNu_HT200to400  WJetsToLNu_HT200to400_ext  WJetsToLNu_HT400to600 WJetsToLNu_HT600to800 WJetsToLNu_HT800to1200 WJetsToLNu_HT800to1200_ext  WJetsToLNu_HT1200to2500  WJetsToLNu_HT2500toInf 
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   WJetsToQQ_HT600toInf      WJetsToQQ_HT180
fi

if  $z
then
  echo ----------------------  Submitting ZJets  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL    ZJetsToNuNu_HT100to200_ext  ZJetsToNuNu_HT200to400_ext  ZJetsToNuNu_HT400to600    ZJetsToNuNu_HT600to800 ZJetsToNuNu_HT800to1200 ZJetsToNuNu_HT1200to2500 ZJetsToNuNu_HT1200to2500_ext  ZJetsToNuNu_HT2500toInf  

  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL     ZJetsToNuNu_HT800to1200  


fi

if  $qcd
then
  echo ----------------------  Submitting QCD  -----------------------
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  QCD_HT100to200 QCD_HT200to300  QCD_HT300to500  QCD_HT500to700 QCD_HT700to1000 QCD_HT1000to1500  QCD_HT1500to2000  QCD_HT2000toInf  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  QCD_HT300to500  QCD_HT300to500_ext QCD_HT500to700_ext  QCD_HT700to1000  QCD_HT700to1000_ext  QCD_HT1000to1500  QCD_HT1000to1500_ext  QCD_HT1500to2000  QCD_HT1500to2000_ext  QCD_HT2000toInf  QCD_HT2000toInf_ext
fi

if  $sig
then
  echo ----------------------  Submitting Priv Signal  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL --inputDBS="phys03" T2DegStop_300_290_FastSim   T2DegStop_300_240_FastSim   T2DegStop_300_270_FastSim  T2tt_300_270_FastSim   
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL --inputDBS="phys03"    T2DegStop_300_270
fi

if  $degstop
then
  echo ------------------------------- Signal Deg Stop -----------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2tt_dM_10to80_genHT_160_genMET_80
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1
fi

if  $ewikino
then
  echo ------------------------------- Signal EWikino -----------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL   SMS_TChiWZ_ZToLL   SMS_TChipmWW 
fi

if  $st
then
  echo ----------------------  Submitting Single Tops  -----------------------
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  T_tWch   TBar_tWch    T_tch  TBar_tch  TToLeptons_tch_powheg TBarToLeptons_tch_powheg TToLeptons_sch_amcatnlo
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  T_tWch   TBar_tWch    T_tch  TBar_tch  #TToLeptons_tch_powheg TBarToLeptons_tch_powheg TToLeptons_sch_amcatnlo
fi

if  $qcdpt
then
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  QCD_Pt15to20_EMEnriched QCD_Pt20to30_EMEnriched QCD_Pt30to50_EMEnriched QCD_Pt50to80_EMEnriched QCD_Pt80to120_EMEnriched  QCD_Pt120to170_EMEnriched  QCD_Pt170to300_EMEnriched  QCD_Pt300toInf_EMEnriched  QCD_Pt15to20_Mu5  QCD_Pt20to30_Mu5  QCD_Pt50to80_Mu5 QCD_Pt80to120_Mu5   QCD_Pt120to170_Mu5   QCD_Pt300to470_Mu5  QCD_Pt470to600_Mu5  QCD_Pt600to800_Mu5  QCD_Pt800to1000_Mu5  QCD_Pt1000toInf_Mu5  QCD_Pt10to15  QCD_Pt15to30  QCD_Pt30to50  QCD_Pt50to80  QCD_Pt80to120  QCD_Pt120to170  QCD_Pt170to300  QCD_Pt300to470  QCD_Pt470to600  QCD_Pt600to800  QCD_Pt800to1000  QCD_Pt1000to1400  QCD_Pt1400to1800  QCD_Pt1800to2400  QCD_Pt2400to3200  QCD_Pt3200toInf QCD_Pt30to50_Mu5
fi

if  $vv
then
  echo ----------------------  Submitting Dibosons  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL WW WZ ZZ #TBar_tWch  T_tWch 
fi

if  $ttx
then
  echo ----------------------  Submitting Dibosons  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  TTWToLNu TTWToQQ TTW_LO TTZToQQ TTZToLLNuNu TTZ_LO TTGJets 
fi

if  $dy

then
  echo ----------------------  Submitting DY  -----------------------
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  DYJetsToLL_M50_HT100to200_ext  DYJetsToLL_M50_HT200to400_ext DYJetsToLL_M50_HT200to400_ext DYJetsToLL_M50_HT400to600_ext DYJetsToLL_M50_HT600toInf  DYJetsToLL_M50_HT600toInf_ext  # DYJetsToLL_M50_HT100to200_ext DYJetsToLL_M50_HT200to400_ext  DYJetsToLL_M50_HT400to600_ext  DYJetsToLL_M50_HT600toInf  DYJetsToLL_M50_HT600toInf_ext
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  DYJetsToLL_M5to50_LO         DYJetsToNuNu_M50  
  python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  DYJetsToLL_M5to50_HT100to200 DYJetsToLL_M5to50_HT100to200_ext DYJetsToLL_M5to50_HT200to400 DYJetsToLL_M5to50_HT200to400_ext DYJetsToLL_M5to50_HT400to600 DYJetsToLL_M5to50_HT600toInf DYJetsToLL_M5to50_HT600toInf_ext #DYJetsToLL_M5to50_HT100to200 DYJetsToLL_M5to50_HT200to400  DYJetsToLL_M5to50_HT400to600  DYJetsToLL_M5to50_HT600toInf 
  #python launch.py  --unitsPerJob=1 --remoteDir=$REMOTE_DIR_MC --production_label=$PROD_LABEL  DYJetsToLL_M50_HT100to200    DYJetsToLL_M50_HT200to400     DYJetsToLL_M50_HT400to600     DYJetsToLL_M50_HT600toInf  
fi


