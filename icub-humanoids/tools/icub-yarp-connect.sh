#!/bin/bash

echo "== Connecting YARP ports =="

yarp connect /icub/left_arm/state:o /iCubGui/left_arm:i
yarp connect /icub/right_arm/state:o /iCubGui/right_arm:i
yarp connect /icub/torso/state:o /iCubGui/torso:i
yarp connect /icub/head/state:o /iCubGui/head:i
yarp connect /icub/camcalib/left/out /leftCam
yarp connect /icub/camcalib/right/out /rightCam
yarp connect /icub/left_arm/state:o /icub-humanoids/left_arm_dumper
yarp connect /icub/right_arm/state:o /icub-humanoids/right_arm_dumper

sleep 1

echo "== YARP Connected =="

while true; do
    echo "Running..."
    sleep 2
done
