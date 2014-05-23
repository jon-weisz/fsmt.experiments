from pymorse import Morse, MorseServicePreempted
import time

with Morse() as simu:
    simu.rpc('human', 'move', 0.2, -1.57)
    time.sleep(2)
    simu.rpc('human', 'move', 0.2, 1.57)

    
