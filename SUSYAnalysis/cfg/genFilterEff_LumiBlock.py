import ROOT

#import ROOT; a  = ROOT.TChain("Events"); z= [ a.Add(f) for f in SMS_T2tt_dM_10to80_genHT_160_genMET_80.files ]

from DataFormats.FWLite import Events, Handle, Lumis
import DataFormats.FWLite as FWLite
import os
from copy import deepcopy

keys=[
"numEventsPassed"        ,
"numEventsTotal"        ,
"numEventsTried"        ,
"numPassNegativeEvents"        ,
"numPassPositiveEvents"        ,
"numTotalNegativeEvents"        ,
"numTotalPositiveEvents"        ,
"sumFailWeights"        ,
"sumFailWeights2"        ,
"sumPassWeights"        ,
"sumPassWeights2"        ,
"sumWeights"        ,
"sumWeights2"        ,
"filterEfficiency"        ,
"filterEfficiencyError"        ,
]


keys_to_add=[
"numEventsPassed"              ,
"numEventsTotal"               ,
"numEventsTried"               ,
"numPassNegativeEvents"        ,
"numPassPositiveEvents"        ,
"numTotalNegativeEvents"        ,
"numTotalPositiveEvents"        ,
"sumFailWeights"        ,
"sumFailWeights2"        ,
"sumPassWeights"        ,
"sumPassWeights2"        ,
"sumWeights"        ,
"sumWeights2"        ,
#"filterEfficiency"        ,
#"filterEfficiencyError"        ,
]



import CMGTools.RootTools.samples.samples_13TeV_signals as signals
import multiprocessing


samples = {
            "T2tt_dM_10to80_genHT_160_genMET_80"              : signals.SMS_T2tt_dM_10to80_genHT_160_genMET_80                ,
            "T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1"     : signals.SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1       ,
            "T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1": signals.SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1  ,
          }

sample = "T2tt_dM_10to80_genHT_160_genMET_80"
sample = "T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1"
sample = "T2tt_dM_10to80_genHT_160_genMET_80_mWMin0p1"

fileList = samples[sample].files

#if not fileList and "mWMin0p1" in sample:
if "mWMin0p1" in sample:
  import signal_files
  fileList = getattr(signal_files, "%s_files"%sample)
  print "No Files found in the CMG data set for %s, instead using the predifined files in signal_files"%sample


if not  fileList:
  print "No files found!"
  assert False

badfiles=[
]


for f in fileList:
    if any([badfile in f for badfile in badfiles]):
        fileList.pop( fileList.index(f) )
        print f

#fileList = ["root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/SMS-T2tt_dM-10to80_genHT-160_genMET-80_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/00000/009E3FE0-C24B-E611-896E-002590E1E9B8.root"]

output_dir = "./model_info/"

import pickle



from collections import defaultdict



#model_base_string = "T2tt_dM-10to80_genHT-160_genMET-80_"
model_base_string = sample +"_" 
getMasses = lambda model: map(int, model.replace(model_base_string,"").split("_")[-2:] )

def makeMassDict(masses):
    ret = {}
    for mstop in masses:
        ret[mstop] = {}
        for mlsp in masses[mstop]:
          ret[mstop][mlsp] = masses[mstop][mlsp]
    return ret


Dict = lambda :defaultdict(Dict) 

if __name__ == '__main__':

    x=0
    class Counter(object):
        def __init__(self):
            self.n = 0
            return
        def next(self):
            self.n +=1
            return self.n

    counter = Counter()


    def getModelInfoFromFile(f):
        #events =  Events(f)
        lumis  =  FWLite.Lumis(f)
        models = {}
        #tree = ROOT.TChain("Events")
        #if type(f)==type(""):
        #    tree.Add(f)
        #else:
        #    for ff in f:
        #        tree.Add(ff)
        #events.toBegin()
        #print "number of Events: "
        #nEvents = tree.GetEntries()
        #print nEvents
        n = counter.next()
        print n
        for lumi in lumis:
            genLumiInfoHandle = Handle( "<GenLumiInfoHeader>" )
            lumi.getByLabel( "generator" , genLumiInfoHandle )
            genLumiInfo = genLumiInfoHandle.product()
            model = genLumiInfo.configDescription()
            genFilterInfoHandle = Handle("<GenFilterInfo>")
            lumi.getByLabel( "genFilterEfficiencyProducer" , genFilterInfoHandle )
            genFilterInfo = genFilterInfoHandle.product()
            info ={}
            for key in keys_to_add:
                info[key] = getattr(genFilterInfo,key)()
            if not models.get(model): 
                models[model]=info
            else:
                for key in info:
                  models[model][key] += info[key]
            #print ievt, models
        filename= os.path.splitext(os.path.basename(f))[0]
        pickle.dump( models, open( output_dir +"/models_info_file_%s_%s.pkl"%(sample,filename),"w"))
        #print models
        return models


    nProc = 30
    if nProc:
        print sample
        print "number of files: %s"%len(fileList)
        print "This will take some time! grab a coffee and finish the other thing you were working on!"
        pool = multiprocessing.Pool(nProc)
        results = pool.map( getModelInfoFromFile ,  fileList)
        pool.close()
        #pool.join()
        #models = {}
        #for res in results:
        #    for model, info in res.iteritems():
        #        if not models.get(model): models[model]={}
        #        for key in keys_to_add:
        #            if models.has_key(key):
        #                models[model][key] += info[key]
        #            else:
        #                models[model][key]  = info[key]
    else:
        models = getModelInfoFromFile(fileList)            



    
    masses = Dict()
    for res in results:
        for model in res:
            mstop, mlsp = getMasses(model)
            masses[mstop][mlsp] = 0
    massDict = dict(deepcopy(masses))


    filterEffs  =   makeMassDict(masses)
    filterPass  =   makeMassDict(masses)
    filterTot   =   makeMassDict(masses)
    
    for res in results:
        for model, info in res.iteritems():
            mstop,mlsp = getMasses(model)
            filterTot[mstop][mlsp]  += info['numEventsTotal']
            filterPass[mstop][mlsp] += info['numEventsPassed']

    for mstop in masses.keys():
        for mlsp in masses[mstop].keys():
            filterEffs[mstop][mlsp]=  1.* float( filterPass[mstop][mlsp]) / float( filterTot[mstop][mlsp] )

    filterEffTitle = "filterEffs_%s"%sample
    pickle.dump( filterEffs , open("filterEffs_%s.pkl"%sample,"w"))

    makePlot = True
    if makePlot:
        plot_save_dir = "/afs/hephy.at/user/n/nrad/www/signals/80X/filterEffs/"

        from Workspace.DegenerateStopAnalysis.tools.degTools import makeStopLSPPlot, setup_style
        setup_style()
        ROOT.gStyle.SetPaintTextFormat("0.3f")
        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextSize(0.038)

        binning = [ 23, 237.5, 812.5, 63, 167.5, 795]
        plt = makeStopLSPPlot( filterEffTitle, filterEffs , bins = binning)
        c1 = ROOT.TCanvas("c1","c1", 1600, 900)
        plt.Draw("COLZ TEXT")
        latex.DrawLatex(0.2,0.85, "Gen. Filter Efficiency")
        latex.DrawLatex(0.2,0.8, sample)
        c1.SaveAs( plot_save_dir + "/" + filterEffTitle + ".png")
        c1.SaveAs( plot_save_dir + "/" + filterEffTitle + ".root")
        pickle.dump( filterEffs , open(plot_save_dir + "/%s.pkl"%filterEffTitle,"w"))

    #pickle.dump( models, open( output_dir +"/models_evts.pkl", "w"))
    
