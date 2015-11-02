#!/usr/bin/env python

import os
import time

sourcePath = [ '/data/nginx/logs/', 'zplayworld.access.log', 'nginx.pid' ]
strDate = time.strftime('%Y%m%d')
cmd = 'cd %s && /bin/mv %s %s.%s && /bin/kill -USR1 `cat %s/%s`' % (sourcePath[0], sourcePath[1], sourcePath[1], strDate, sourcePath[0], sourcePath[2])

if os.system(cmd) == 0:
        print 'nginx Cut Log Successful.'
else:
        print 'nginx Cut Log failure.'
