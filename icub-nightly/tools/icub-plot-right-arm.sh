#!/bin/bash

/usr/bin/gnuplot <<__EOF
reset
set terminal png
set xlabel "frame [yarp]"
set ylabel "joint value [degree]"
set title "iCub-Nightly Balltracking right_arm"
set key below
set grid
set style data lines
set output '/tmp/$USER/fsmt/$FSMTRA/icub-right-arm.png'
plot '$prefix/etc/fsmt-experiments/icub-nightly/reference-data/right_arm.dump' using :2 with lines title "reference right_arm[1]", \
'$1' using :2 with lines title "right_arm[1]"
__EOF