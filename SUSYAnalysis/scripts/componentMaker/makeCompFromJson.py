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

component_template =    "{pname}     =   kreator.makeDataComponent(\"{pname}\" , \"{dataset_name}\" , \"CMS\", \".*root\", json) "

l = []
for data_info in data_list:
    dataset_info = data_info['dataset']
    if len(dataset_info) != 1: 
        print dataset_info
        assert False
    dataset_info = dataset_info[0]
    dataset_name = dataset_info['name']
    blank, primary , processed, tier = dataset_info['name'].rsplit("/")
    pname = "_".join([x.replace("-","_") for x in [primary, processed]])
    #print JetHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v2"         , "/JetHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
    if primary not in samples_to_use:
        continue
    print component_template.format(pname=pname, dataset_name = dataset_name)
    l.append(pname)


print "\n" , "samples = " , "[ %s ] "% ' , '.join([p for p in l])
    

    
