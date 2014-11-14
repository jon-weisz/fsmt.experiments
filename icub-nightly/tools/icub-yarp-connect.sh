#!/bin/bash

echo "== Connecting YARP ports =="

sleep 1

`yarp connect /icub/left_arm/state:o /iCubGui/left_arm:i`
`yarp connect /icub/right_arm/state:o /iCubGui/right_arm:i`
`yarp connect /icub/torso/state:o /iCubGui/torso:i`
`yarp connect /icub/head/state:o /iCubGui/head:i`
`yarp connect /icub/camcalib/left/out /leftCam`
`yarp connect /icub/camcalib/right/out /rightCam`

sleep 1

`yarp read /icub-nightly/right_arm_dumper | tee $FSMBASE/logs/right_arm.dump` &
`yarp read /icub-nightly/left_arm_dumper | tee $FSMBASE/logs/left_arm.dump` &
`yarp connect /icub/right_arm/state:o /icub-nightly/right_arm_dumper > /dev/null 2>&1`
`yarp connect /icub/left_arm/state:o /icub-nightly/left_arm_dumper > /dev/null 2>&1`

echo "== YARP Connected =="

while true; do
    echo "Running..."
    sleep 3
done


# Not used, yet.
# /icub/inertial
# yarp connect /icub/right_leg/state:o /iCubGui/right_leg:i
# yarp connect /icub/left_leg/state:o /iCubGui/left_leg:i
