__author__ = 'flier'

import os
import sys
import time
import pymorse

sys.path.append('/opt/strands-morse-simulator/lib/python3/dist-packages/')

with pymorse.Morse() as sim:
    sim.rpc('simulation', 'set_camarafp_position' [10, 10, 10])

while True:
    time.sleep(10)