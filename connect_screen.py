#!/usr/bin/env python3
import subprocess
from subprocess import DEVNULL, STDOUT, check_call

import shlex
import os
import time



def run_command(cmd):
#    print("\n\n\n\n", cmd, "\n\n\n\n")
#    check_call([cmd], stdout=DEVNULL, stderr=DEVNULL)
    os.system(cmd)


while True:
    #--- set both commands (connect / disconnect) below
    id = subprocess.getoutput('xinput | grep "Silicon Works Multi-touch SW4101C" | cut -f 2 | cut -c 4-9 | tail -n +2')
    if id != "":
        connect_command = "xinput map-to-output " +  id + " DP-1"
        run_command(connect_command)
        
    time.sleep(15)
