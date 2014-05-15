#!/usr/bin/python

__author__ = 'flier'

import sys
import subprocess


class Grapher:

    def __init__(self, filepath, var):
        self.var = var
        self.filepath = filepath
        self.resultfile = open('/tmp/oncilla-result.csv', 'w')
        self.resultfile.write("step, " "value \n")
        self.read_file()

    def add_to_file(self, data):
        self.resultfile.write(data)

    def create_graph(self):
        pass

    def read_file(self):
        with open(self.filepath) as f:
            step = 0
            for line in f:
                if "x:" in line and not "qx:" in line:
                    line = line.replace(" ", "")
                    line = line.replace("x:", "")
                    line = str(step)+", " + line
                    step += 1
                    self.add_to_file(line)

    def plot(self):
        p = subprocess.call("plot-sine.sh")

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print "You need to provide a full path to oncilla log file"
        sys.exit(1)
    g = Grapher(sys.argv[1], "x")
    g.resultfile.close()
    g.plot()