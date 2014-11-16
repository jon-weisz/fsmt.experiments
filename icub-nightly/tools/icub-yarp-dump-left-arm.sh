#!/bin/bash

echo "== Reading YARP ports =="

yarp read /icub-nightly/left_arm_dumper | tee $FSMBASE/logs/left_arm.dump

while true; do
    sleep 2
done
