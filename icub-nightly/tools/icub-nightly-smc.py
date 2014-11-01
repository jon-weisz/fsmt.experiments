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
props.put("local", "/client_put/right_arm")
props.put("remote", "/icubSim/right_arm")

# Create remote driver
arm_driver = yarp.PolyDriver(props)

# Query motor control interfaces
i_pos = arm_driver.viewIPositionControl()
i_vel = arm_driver.viewIVelocityControl()
i_enc = arm_driver.viewIEncoders()

# Retrieve number of joints
jnts = i_pos.getAxes()

print '>> Controlling', jnts, 'joints'

# Read encoders
encoders = yarp.Vector(jnts)

i_enc.getEncoders(encoders.data())

# Store as home position
home = yarp.Vector(jnts, encoders.data())

# Initialize a new tmp vector identical to encoders
tmp = yarp.Vector(jnts)

tmp.set(0, tmp.get(0)+40)
tmp.set(1, tmp.get(1)+30)
tmp.set(2, tmp.get(2)+20)
tmp.set(3, tmp.get(3)+10)

print '>> Setting new Joint values'

i_pos.positionMove(tmp.data())

time.sleep(5)

print '>> Setting inital Joint values'

tmp_n = yarp.Vector(jnts)

tmp_n.set(0, tmp.get(0)-40)
tmp_n.set(1, tmp.get(1)-30)
tmp_n.set(2, tmp.get(2)-20)
tmp_n.set(3, tmp.get(3)-10)

# Go back to initial position
i_pos.positionMove(tmp_n.data())

print '>> Exiting'
