from morse.builder import *

# Adding the Robot ATRV
robot = ATRV()
robot.translate(x=0.8, z=0.2)
robot.rotate(x=0.0, y=0.0, z=3.14)

# Adding the Robot's differential drive actuator 
motion_vw = MotionVW()
robot.append(motion_vw)

# Adding a waypoint Actuator
waypoint = Waypoint()
waypoint.properties(ObstacleAvoidance = False, ControlType = "Position")

# Adding a Pose sensor
pose = Pose()

# Adding Passive Objects
box_blue = PassiveObject('props/objects','BlueToyTrashbin')
box_blue.setgraspable()
box_blue.translate(x=0.5, y=-2.0, z=0.0)
box_blue.rotate(z=0.2)

box_pink = PassiveObject('props/objects','PinkToyTrashbin')
box_pink.setgraspable()
box_pink.translate(x=1.0, y=-2.0, z=0.0)
box_pink.rotate(z=0.25)

# Properties for the Passive Objects
box_blue.properties(Object = True, Graspable = False, Label = "BOX_BLUE")
box_pink.properties(Object = True, Graspable = False, Label = "BOX_PINK")

# Adding a Human Component
human = Human()
human.translate(x=-1.0, z=0.0)
human.use_world_camera()
human.disable_keyboard_control()
human.append(waypoint)
human.append(pose)

# Properties for the Human Object
human.properties(Object = True, Graspable = False, Label = "HUMAN")

# Add a Video Stream
video_cam = VideoCamera()
video_cam.translate(0.0, 0.0, 1.2)
video_cam.rotate(y=-0.25)

# Semantic camera
semantic = SemanticCamera()
semantic.properties(cam_focal = 50, cam_far = 200, noocclusion = True)
semantic.translate(x=0.0, y=0.0, z=1.3)
robot.append(semantic)
robot.append(video_cam)

# Middleware Interfaces
semantic.add_stream('ros')
motion_vw.add_stream('ros')
video_cam.add_stream('ros')
pose.add_stream('socket')
waypoint.add_stream('socket')
human.add_service('socket')

# Environment
env = Environment('apartment')
env.place_camera([10.0, -5.0, 10.0])
env.aim_camera([1.0470, 0, 0.7854])
