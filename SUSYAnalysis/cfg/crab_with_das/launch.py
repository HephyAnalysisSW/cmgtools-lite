#! /usr/bin/env python
import imp, os, sys
from optparse import OptionParser

# datasets to run as defined from run_susyMT2.cfg
# number of jobs to run per dataset decided based on splitFactor and fineSplitFactor from cfg file
# in principle one only needs to modify the following two lines:

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label", help="production label", default="heppy")
parser.add_option("--remoteDir", dest="remoteDir", help="remote subdirectory", default="")
parser.add_option("--cmg_version", dest="cmg_version", help="CMG version", \
                      default="CMGTools-from-CMSSW_8_0_11")
parser.add_option("--unitsPerJob", dest="unitsPerJob", help="Nr. of units (files) / crab job", type="int", default=1)
parser.add_option("--totalUnits", dest="totalUnits", help="Total nr. of units (files)", type="int", default=None)
parser.add_option("--inputDBS", dest="inputDBS", help="dbs instance", default=None)
parser.add_option("--lumiMask", dest="lumiMask", help="lumi mask (for data)", default=None)
( options, args ) = parser.parse_args()

handle = open("heppy_samples.py", 'r')
cfo = imp.load_source("heppy_samples", "heppy_samples.py", handle)
handle.close()

import PhysicsTools.HeppyCore.framework.config as cfg
allComponents = { }
for d in cfo.__dict__:
    c = cfo.__dict__[d]
    if isinstance(c,cfg.Component):
        if c.name in allComponents:
            print "Ignoring duplicate component: variable name = ",d," component name = ",c.name
        allComponents[c.name] = c
        

selectedComponents = [ ]
for c in args:
    if c in allComponents:
        selectedComponents.append(allComponents[c])
    elif c in cfo.__dict__ and type(cfo.__dict__[c]) == type([]):
        for cc in cfo.__dict__[c]:
          if cc in allComponents.itervalues():
            selectedComponents.append(cc)
    else:
        print "*** Skipping undefined component: ",c
if not selectedComponents:
    print "Did not find any matching component! Available components are"
    for c in sorted(allComponents.keys()):
        print "   ",c
    sys.exit(1)

os.system("scram runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

os.environ["CMG_PROD_LABEL"]  = options.production_label
os.environ["CMG_REMOTE_DIR"]  = options.remoteDir
os.environ["CMG_VERSION"] = options.cmg_version
os.environ["CMG_UNITS_PER_JOB"] = str(options.unitsPerJob)
os.environ["CMG_LUMI_MASK"] = options.lumiMask if options.lumiMask else "None"
if options.totalUnits:
    os.environ["CMG_TOTAL_UNITS"] = str(options.totalUnits)
else:
    if "CMG_TOTAL_UNITS" in os.environ:
        del os.environ["CMG_TOTAL_UNITS"]
if options.inputDBS:
    os.environ["INPUT_DBS"] = options.inputDBS

#from PhysicsTools.HeppyCore.framework.heppy import split
import pickle
for comp in selectedComponents:
#    print "generating sample_"+comp.name+".pkl"
    print "Processing ",comp.name
    #comp.splitFactor = 1
    #comp.fineSplitFactor = 1
    fout = open("sample_"+comp.name+".pkl","wb")
    pickle.dump(comp,fout)
    fout.close()
#    os.environ["DATASET"] = str(comp.name)
    os.environ["CMG_DATASET"] = comp.dataset
    if hasattr(comp, "json") and comp.json:
        os.environ["CMG_JSON"] = os.path.expandvars(comp.json)
    os.environ["CMG_COMPONENT_NAME"] = comp.name
#    os.system("python tmp.py > tmp.lis")
    os.system("which crab")
    os.system("crab submit -c heppy_crab_config_env.py")



def makeCMGComponentList(tag, selectedComponents, dpm_path =""):
    #summary_file = "./%s_CMGComponents.pkl"%tag
    summary_file = "./%s.pkl"%tag
    if os.path.isfile(summary_file):
        sample_summary = pickle.load(open(summary_file,'r'))
    else:
        sample_summary = {}
    for comp in selectedComponents:
        compName =  allComponents.keys()[allComponents.values().index(comp)]  
        if not sample_summary.has_key(compName):
            comp.production_label     = options.production_label
            comp.remote_dir           = options.remoteDir
            sample_summary[compName]  = comp
    pickle.dump( sample_summary, open( summary_file, 'w' ) )
    if dpm_path:
        os.system("/usr/bin/rfcp  {summary_file}  {dpm_path}/{summary_file}".format(summary_file = summary_file , dpm_path = dpm_path))

makeCMGComponentList( options.production_label , selectedComponents)



#for comp in selectedComponents:
#    print comp


#os.system("rm -f python.tar.gz")
#os.system("rm -f cmgdataset.tar.gz")
#os.system("rm -f cafpython.tar.gz")
