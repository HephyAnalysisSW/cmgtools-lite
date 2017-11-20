import PhysicsTools.HeppyCore.framework.config as cfg
import subprocess
import os.path

from RootTools.fwlite.Database import Database

def makeDPMGetFileListFunction(name, dpmdir, subdirs, server, verbose):
    def Func( name=name, dpmdir=dpmdir, subdirs=subdirs,server=server, verbose=verbose  ):
        basedir="root://%s/"%server
        prot="xrd"
        dpmdir = "/cms/"+dpmdir
        lscommand= prot + " " + server + "  ls  " +dpmdir
        dirs={}
        allfiles=[]
        cache = Database("signal_cache.db", "fileCache", ["name"])
        nFiles = cache.contains({'name':name})
        if nFiles:
            print 'Found sample in cache, adding %i file'%nFiles
            files = cache.getDicts({'name':name})
            for f in files:
                allfiles.append(f["value"])
        else:
            for subdir in subdirs:
                #gfalout  = subprocess.Popen(["gfal-ls "+ basedir+"/"+dpmdir+'/'+subdir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                lsout = subprocess.Popen([ lscommand ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for f in lsout.stdout.readlines():
                    f =  f.rsplit()
                    if len(f)==0:
                        continue
                    f=f[-1]
                    if not f.endswith("root"):
                        continue
    return Func

def makePrivateMCComponentFromDPM(name,dataset,dpmdir,subdirs=[''],xSec=1,server= "hephyse.oeaw.ac.at",verbose=False):
    getFilesFunc=makeDPMGetFileListFunction(name, dpmdir, subdirs, server, verbose)

    component = cfg.MCComponent(
        dataset=dataset,
        name = name,
        files = getFilesFunc(),
        xSection = xSec,
        nGenEvents = 1,
        triggers = [],
        effCorrFactor = 1,
    )
    if verbose:
      print "%s , xSec:%s , dataset: %s " %(name, xSec, dataset)
      print "    Component:", component
    return component

