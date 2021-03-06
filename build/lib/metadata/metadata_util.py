

from subprocess import check_output

import time
import datetime

#
#  Gets the process id of java
#
# print get_pid('java')

#
def get_pid(name):
    return check_output(["pidof",name])

def get_current_time():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


