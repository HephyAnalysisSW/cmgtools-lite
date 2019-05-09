#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.StopsDilepton.samples import *
from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
from CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2 import *
#from CMGTools.StopsDilepton.Higgs_signals_RunIISummer16MiniAODv2 import *
#from CMGTools.StopsDilepton.ewkDM_signals_RunIISummer16MiniAODv2 import *
from CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2 import *
from CMGTools.RootTools.samples.samples_13TeV_signals import *

for sample in dataSamples + samples_data_private:
    sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
