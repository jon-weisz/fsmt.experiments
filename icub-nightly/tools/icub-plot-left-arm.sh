#!/bin/bash

/usr/bin/gnuplot <<__EOF
reset
set terminal png
set xlabel "step [yarp]"
set ylabel "joint value [degree]"
set title "iCub-Nightly Balltracking left_arm"
# set key reverse Left outside
set key below
set grid
set style data points
set output '/tmp/$USER/fsmt/$FSMTRA/icub-left-arm.png'
plot '$1' using :2 with linespoints title "left_arm[1]", \
'$prefix/etc/fsmt-experiments/icub-nightly/reference-data/left_arm.dump' using :2 with points title "reference left_arm[1]"
__EOF