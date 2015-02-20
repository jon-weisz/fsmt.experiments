__author__ = 'flier'

import os
import sys
import time
from Tkinter import *


logpath = os.environ['FSMLOG']
logfile = logpath + "personchecker.log"
persons_found = {'linus': False, 'bill': False, 'dennis': False, 'steve': False}
test_failed = False

with open(logfile) as f:
    for line in f:
        if ">> Found Linus!" in line:
            persons_found['linus'] = True
        if ">> Found Bill!" in line:
            persons_found['bill'] = True
        if ">> Found Steve!" in line:
            persons_found['steve'] = True
        if ">> Found Dennis!" in line:
            persons_found['dennis'] = True

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(400, 50))
text = Text(root)

for key, value in persons_found.iteritems():
    if not value:
        print "Could not find: " + key
        test_failed = True
        sys.exit(1)

print "Test Passed --- Found: Linus, Bill, Steve and Dennis "

text.insert(INSERT, "Test Passed --- Found: Linus, Bill, Steve and Dennis ")
text.pack()
text.tag_add("here", "1.0", "10.0")
text.tag_config("here", foreground="green")

if __name__ == "__main__":
    root.mainloop()