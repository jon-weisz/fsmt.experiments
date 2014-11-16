#!/bin/bash

/usr/bin/gnuplot <<__EOF
reset
set terminal png
set xlabel "step"
set ylabel "joint value"
set title "iCub-Nightly Balltracking left_arm"
set key reverse Left outside
set grid
set style data linespoints
set output '/tmp/$USER/fsmt/$FSMTRA/icub-left-arm.png'
plot '$1' using :2 with linespoints title "left_arm[1]"
plot $prefix/etc/fsmt-experiments/icub-nightly/reference-data/left_arm.dump using :2 with linespoints title "reference left_arm[1]"
__EOF