#! /usr/bin/gnuplot

name="/tmp/oncilla-result.csv"
set title "Oncilla-Sim-0.2-Sine"
set xlabel "Time Step"
set ylabel "X Position in Metres"
set term png
set output "/tmp/oncilla-sine-result.png"
plot name using 1:2 with linespoints notitle

name="/tmp/oncilla-result.csv"
set title "Oncilla-Sim-0.2-Sine"
set xlabel "Time Step"
set ylabel "X Position in Metres"
set term x11
set out
plot name using 1:2 with linespoints notitle
pause -1
