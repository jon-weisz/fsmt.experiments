__author__ = 'flier'

import time
import pymorse

with pymorse.Morse() as sim:
    sim.rpc('simulation', 'set_camarafp_position' [10, 10, 10])

while True:
    time.sleep(10)