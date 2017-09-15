import glob
import subprocess
import re
import multiprocessing

pattern = "crab_8025_mAODv2_v7_*/*"

crab_base_dir = "./crab_with_das/"



commands = {
            'crb'   : 'crab'    ,
            'sts'   : 'status'  , 
            'rsub'  : 'resubmit',
            }

crab_status   = ['crab', 'status']
crab_resubmit = ['crab', 'resubmit']

sitewhitelists= [] 


errors = ['Cannot find .requestcache file in CRAB project directory' ]



from optparse import OptionParser
from collections import OrderedDict
parser = OptionParser()

parser.add_option("--pattern"   , dest="pattern", default = "crab_8020_mAODv2_v5_*/*"  , help="Pattern for crab directories")
parser.add_option("--base_dir"  , dest="crab_base_dir", default = "./crab_with_das/"  , help="Base directory for crab output directories")
parser.add_option("--state"     , dest="state", default = ""  , help="Print output with this state")
parser.add_option("--finished"  , dest="finished", default = False , action="store_true"  , help="Show jobs that are 100% finished")
parser.add_option("--unfinished"  , dest="unfinished", default = False , action="store_true"  , help="Show jobs that are not 100% finished")


parser.add_option("--resubmit"  , dest="resubmit", default = False , action="store_true"  , help="Resubmit directories with any failed jobs")



(options,args) = parser.parse_args()


crab_base_dir =   options.crab_base_dir
patter        =   options.pattern

crab_dirs = glob.glob(crab_base_dir + pattern )

crab_states = ['submitted', 'running', 'transfering', 'finished', 'cooloff', 'failed', 'idle']

if options.state and options.state not in crab_states:
    raise Exception( "State, %s, is not one of the recognized crab states:%s,"%(options.state, crab_states))
#status = { state:{'%':0, 'r':'(0/0)'} for state in crab_states}
dirs_of_interest = []

failed_jobs = []
incomp_jobs = []
unknowns    = []

def resubmit_crab_job(crab_dir):
  subproc_stdout = subprocess.Popen( crab_resubmit +[crab_dir] + sitewhitelists , stdout=subprocess.PIPE )
  out = subproc_stdout.communicate()
  return out

def getCrabDirStatus( crab_dir ):
    subproc_stdout = subprocess.Popen( crab_status +[crab_dir], stdout=subprocess.PIPE )
    stdout , err = subproc_stdout.communicate()
    status = {}
    for state in crab_states:
        st = re.search( state +".*", stdout)
        if st:
            a = st.group().rsplit()
            a1 = a.pop(0)
            a2 = a.pop(0)
            a3 = ''.join(a)
            #print a
            #assert all( [a1 == state , r'%' in a2] )
            status[state]={}
            status[state]['%'] = a2.replace(r'%','')
            status[state]['r'] = a3
    corrupted_dir = any([x in stdout for x in errors])

    if not status and not corrupted_dir:
        print stdout
        unknowns.append(crab_dir)

        #corrupted_dirs.append(crab_dir)
    return {'status':status, 'stdout':stdout , 'isCorrupted':corrupted_dir}


def resubmit_forever( crab_dirs ):
    for crab_dir in crab_dirs:
        print 'resubmiting.....', crab_dir
        resubmit_crab_job( crab_dir )

corrupted_dirs =[]
results = {}
finished_jobs = []



nProcesses = 3

if nProcesses >1 :
    pool = multiprocessing.Pool(processes=nProcesses)
    results_paral = pool.map( getCrabDirStatus, crab_dirs)
    pool.close()
    pool.join()


#for crab_dir in crab_dirs:
#  results[crab_dir] = getCrabDirStatus( crab_dir )

results = dict( zip( crab_dirs , results_paral  ))
for crab_dir in crab_dirs:
  status = results[crab_dir]['status'] 
  stdout = results[crab_dir]['status']
 
  if results[crab_dir]['isCorrupted'] : 
      corrupted_dirs.append(crab_dir)
  

  doPrint      =  False
  failed_job   =  False
  finished_job =  False
  incomp_job   =  False

  if "finished" in status and status['finished'][r'%']=='100.0':
      finished_jobs.append(crab_dir)
      finished_job = True
  elif 'failed' in status:
      failed_job = True
      failed_jobs.append(crab_dir)
  else:
      incomp_job  = True
      incomp_jobs.append(crab_dir)

  if options.finished and finished_job:
      doPrint = True
  elif options.unfinished and incomp_job:
      doPrint = True
  elif options.state:
      if options.state in status:
          doPrint = True
  else:       
      doPrint = False


  if doPrint: 
      dirs_of_interest.append(crab_dir)
      print "-----  ", crab_dir
      print stdout
      print

  if options.resubmit :
      resubmit_crab_job( crab_dir)

print "These CRAB Directories seem to be corrupted or in compelete"
print corrupted_dirs
