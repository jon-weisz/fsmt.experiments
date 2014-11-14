#!/bin/bash

echo "== Connecting yarp ports =="

yarp connect /icub/left_arm/state:o /iCubGui/left_arm:i
yarp connect /icub/right_arm/state:o /iCubGui/right_arm:i
yarp connect /icub/torso/state:o /iCubGui/torso:i
yarp connect /icub/head/state:o /iCubGui/head:i
yarp connect /icub/camcalib/left/out /leftCam
yarp connect /icub/camcalib/right/out /rightCam

echo "== Connected =="

sleep 5

# Not used, yet.
#
#
# /icub/inertial
# yarp connect /icub/right_leg/state:o /iCubGui/right_leg:i
# yarp connect /icub/left_leg/state:o /iCubGui/left_leg:i
