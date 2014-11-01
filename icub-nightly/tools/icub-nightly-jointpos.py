__author__ = 'flier'

# Example taken from :
# http://wiki.icub.org/iCub_documentation/python-motor-control_8py_source.html
# I just made the syntax a little more "pythonic" and removed ";"

import yarp
import time

yarp.Network.init()

# Prepare a property object
props = yarp.Property()
props.put("device", "remote_controlboard")
props.put("local", "/client_poll/right_arm")
props.put("remote", "/icubSim/right_arm")

# Create remote driver
arm_driver = yarp.PolyDriver(props)

# Query motor control interfaces
i_pos = arm_driver.viewIPositionControl()
i_vel = arm_driver.viewIVelocityControl()
i_enc = arm_driver.viewIEncoders()

# Retrieve number of joints
jnts = i_pos.getAxes()

# Read encoders
encoders = yarp.Vector(jnts)

# Print Joint Values
while True:

    i_enc.getEncoders(encoders.data())
    tmp = yarp.Vector(jnts)

    print "All", tmp
    print "right_arm 0, %.4f" % tmp.get(0)
    print "right_arm 1, %.4f" % tmp.get(1)
    print "right_arm 2, %.4f" % tmp.get(2)
    print "right_arm 3, %.4f" % tmp.get(3)

    time.sleep(0.3)
