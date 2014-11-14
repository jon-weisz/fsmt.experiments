#!/bin/bash

/usr/bin/gnuplot <<__EOF
reset
set terminal png
set xlabel "step"
set ylabel "joint value"
set title "iCub-Nightly Balltracking right_arm"
set key reverse Left outside
set grid
set style data linespoints
set output '/tmp/$USER/fsmt/$FSMTRA/icub-left-arm.png'
plot '$1' using :1 with linespoints title "right_arm[0]"
__EOF