import sys
import time


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
                        print "Error, position is not -1.00 but %s" % first
                        time.sleep(5)
                        sys.exit(1)
                if x == leng:
                    last = line[0:5]
                    try:
                        assert float(last) == 0.324
                    except AssertionError, e:
                        print "Error, last is not 0.711 but %s" % last
                        time.sleep(5)
                        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print
        "You need to provide a full path to oncilla-sine log file"
        sys.exit(1)
    g = Checker(sys.argv[1])
    print "All good, position test passed"
    time.sleep(10)
