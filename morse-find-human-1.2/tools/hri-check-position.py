import sys
import unittest


class Checker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.read_file()

    def read_file(self):
        with open(self.filepath) as f:
            for i, l in enumerate(f):
                pass
            leng = i
        with open(self.filepath) as f:
            for x, line in enumerate(f):
                if x == 0:
                    first = line[0:5]
                    try:
                        assert float(first) == -1.00
                    except AssertionError, e:
                        print "Error, position is not -1.00"
                if x == leng:
                    last = line[0:5]
                    try:
                        assert float(last) == 0.593
                    except AssertionError, e:
                        print "Error, last is not 0.593"


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print
        "You need to provide a full path to oncilla-sine log file"
        sys.exit(1)
    g = Checker(sys.argv[1])