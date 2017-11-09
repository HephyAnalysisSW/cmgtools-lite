#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *

for sample in dataSamples:
    sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON.txt"
