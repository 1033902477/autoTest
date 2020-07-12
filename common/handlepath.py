import os, time

basepath = os.path.dirname(os.path.dirname(__file__))


outputfile = os.path.join(basepath, 'output')
logfile = os.path.join(outputfile, 'log')
loglog = os.path.join(logfile, 'loglog.log')

