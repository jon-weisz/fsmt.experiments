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
set output '/tmp/$USER/fsmt/$FSMTRA/icub-right-arm.png'
plot '$1' using :1 with linespoints title "left_arm[0]"
__EOF