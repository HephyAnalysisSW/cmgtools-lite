#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import *

for sample in dataSamples:
    sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
