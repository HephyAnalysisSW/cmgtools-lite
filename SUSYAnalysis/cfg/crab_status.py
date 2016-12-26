import glob
import subprocess
import re


pattern = "crab_8020_mAODv2_v5_*/*"

crab_base_dir = "./crab_with_das/"



commands = {'crb': 'crab'   ,
            'sts': 'status' , 
            'rsub': 'resubmit',
            }

crab_status = ['crab', 'status']






from optparse import OptionParser
from collections import OrderedDict
parser = OptionParser()

parser.add_option("--pattern"   , dest="pattern", default = "crab_8020_mAODv2_v5_*/*"  , help="Pattern for crab directories")
parser.add_option("--base_dir"  , dest="crab_base_dir", default = "./crab_with_das/"  , help="Base directory for crab output directories")
parser.add_option("--state"     , dest="state", default = ""  , help="Print output with this state")
parser.add_option("--finished"  , dest="finished", default = False , action="store_true"  , help="Show jobs that are 100% finished")
parser.add_option("--unfinished"  , dest="unfinished", default = False , action="store_true"  , help="Show jobs that are not 100% finished")



(options,args) = parser.parse_args()


crab_base_dir =   options.crab_base_dir
patter        =   options.pattern

crab_dirs = glob.glob(crab_base_dir + pattern )

crab_states = ['submitted', 'running', 'transfering', 'finished', 'cooloff', 'failed', 'idle']

if options.state and options.state not in crab_states:
    raise Exception( "State, %s, is not one of the recognized crab states:%s,"%(options.state, crab_states))
#status = { state:{'%':0, 'r':'(0/0)'} for state in crab_states}
all_status  = OrderedDict()
all_stdouts = OrderedDict()
for crab_dir in crab_dirs:

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
          assert all( [a1 == state , r'%' in a2] )
          status[state]={}
          status[state]['%'] = a2.replace(r'%','')
          status[state]['r'] = a3
  all_status[crab_dir] = status
  all_stdouts[crab_dir] = stdout


  doPrint=False
  if options.finished:
      if "finished" in status and status['finished'][r'%']=='100.0':
          doPrint = True
  elif options.unfinished:
      if not "finished" in status or ( "finished" in status and  status['finished'][r'%']!='100.0'):
          doPrint = True
  elif options.state:
      if options.state in status:
          doPrint = True
  else:       
      doPrint = True


  if doPrint: 
      print "-----  ", crab_dir
      print stdout
      print
