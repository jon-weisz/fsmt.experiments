#!/bin/bash

echo "== Reading YARP ports =="

yarp read /icub-nightly/left_arm_dumper | tee $FSMBASE/logs/left_arm.dump > /dev/null 2>&1

while true; do
    sleep 2
done
