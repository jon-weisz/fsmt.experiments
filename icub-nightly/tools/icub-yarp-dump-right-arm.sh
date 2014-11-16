#!/bin/bash

echo "== Reading YARP ports =="

yarp read /icub-nightly/right_arm_dumper | tee $FSMBASE/logs/right_arm.dump

while true; do
    sleep 2
done
