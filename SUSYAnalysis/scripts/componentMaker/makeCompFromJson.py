"""

get json from from DAS with the json option 

"""

import yaml
import sys

args = sys.argv


#if for arg in sys.argv:
#  if not arg or 'ipython' in arg:
#    continue
#  args.append(arg)
#
#
#if not len(args):
#  f = "Run2016PromptReco.json"
#else:
#  f = sys.argv[0]  

f = "Run2016ReReco.json"
f = "Run2016PromptReco.json"

f = "TTJets_Summer16.json" 
f = "WJets_Summer16.json"
f = "Summer16.json"

json= yaml.safe_load(file(f))

data_list = json['data']


samples_to_use = [
          "SingleMuon",
          "SingleElectron",
          "MET",
          #"MuonEG",
          "JetHT",
          #"HTMHT",
          #"DoubleMuon",
        ]

samples_to_use = [\
"TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"TT_TuneCUETP8M1_13TeV-powheg-pythia8",
"TT_TuneCUETP8M1_13TeV-powheg-pythia8",
"TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"TTTo2L2Nu_13TeV-powheg",
"ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1",
"ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
"ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1",
"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
"TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8",
"TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8",
"tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1",
"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"ZJetsToNuNu_HT-100To200_13TeV-madgraph",
"ZJetsToNuNu_HT-100To200_13TeV-madgraph",
"ZJetsToNuNu_HT-200To400_13TeV-madgraph",
"ZJetsToNuNu_HT-200To400_13TeV-madgraph",
"ZJetsToNuNu_HT-400To600_13TeV-madgraph",
"ZJetsToNuNu_HT-400To600_13TeV-madgraph",
"ZJetsToNuNu_HT-600To800_13TeV-madgraph",
"ZJetsToNuNu_HT-800To1200_13TeV-madgraph",
"ZJetsToNuNu_HT-1200To2500_13TeV-madgraph",
"ZJetsToNuNu_HT-1200To2500_13TeV-madgraph",
"ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph",
"QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
"WWTo2L2Nu_13TeV-powheg",
"WWToLNuQQ_13TeV-powheg",
"WWToLNuQQ_13TeV-powheg",
"WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
"ZZTo2L2Nu_13TeV_powheg_pythia8",
"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8",
"ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8",
"ZZTo2L2Nu_13TeV_powheg_pythia8",
"ZZTo4L_13TeV_powheg_pythia8",
"WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8",
"WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
"WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8",
"WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8",
"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8",
"WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
"WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph",
"ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph",
"ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph",
"ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
"WW_DoubleScattering_13TeV-pythia8",
"WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8",
"WW_TuneCUETP8M1_13TeV-pythia8",
"WZ_TuneCUETP8M1_13TeV-pythia8",
"ZZ_TuneCUETP8M1_13TeV-pythia8",
"WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
"WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
"WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
"ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
"TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",
"TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",
"ttWJets_13TeV_madgraphMLM",
"TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
"TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
]


component_template =    "kreator.makeDataComponent(\"{pname}\" , \"{dataset_name}\" , \"CMS\", \".*root\", json) "

l = []
components = []
for data_info in data_list:
    dataset_info = data_info['dataset']
    if len(dataset_info) != 1: 
        print dataset_info
        assert False
    dataset_info = dataset_info[0]
    dataset_name = dataset_info['name']
    blank, primary , processed, tier = dataset_info['name'].rsplit("/")
    if dataset_info['datatype']=='mc':
      pname = dataset_info['primary_dataset']['name'].replace("-","_") 
    else:
      pname = "_".join([x.replace("-","_") for x in [primary, processed]])
    #print JetHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v2"         , "/JetHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
    if samples_to_use and primary not in samples_to_use:
        continue
    component =  component_template.format(pname=pname, dataset_name = dataset_name) 
    #print "%s = %s"%(pname, component ) 
    components.append((pname,component))
    l.append(pname)

max_pname_length = max([len(x[0]) for x in components ])

for pname, comp in components:
    print ('{pname:<%s}   =   {comp}'%max_pname_length).format(pname=pname, comp = comp)


print "\n" , "samples = " , "[ %s ] "% ' , '.join([p for p in l])
    

    
