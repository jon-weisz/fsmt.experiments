#!/bin/bash

echo "== Reading YARP ports =="

yarp read /icub-humanoids/right_arm_dumper | tee $FSMBASE/logs/right_arm.dump > /dev/null 2>&1

while true; do
    sleep 2
done
