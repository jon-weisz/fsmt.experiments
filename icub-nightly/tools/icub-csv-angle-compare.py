__author__ = 'flier'

import os
import sys
import csv
import time

logpath = os.environ['FSMLOG']

logfile = "/right_arm.dump"
raw_file = logpath + logfile

csv_repr = "/right_arm.csv"
csv_file = logpath + csv_repr

# Create an actual CSV File
with open(raw_file) as infile, open(csv_file, 'w') as outfile:
    outfile.write(infile.read().replace(" ", ", "))

# Accessible representation
joint_2 = []

with open(csv_file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        joint_2.append(float(row[1]))

last = len(joint_2)
first_value = joint_2[0]
last_value = joint_2[last - 1]

time.sleep(2)

if first_value < 25.0 or first_value > 35.0:
    print "First joint value is off by 5 degree: %s" % str(first_value)
    sys.exit(1)

if last_value < 25.0 or last_value > 35.0:
    print "Last joint value is off by 5 degree: %s" % str(first_value)
    sys.exit(1)

print "First and last joint values are correct"

while True:
    time.sleep(2)