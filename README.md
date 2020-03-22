# ECE470-project
Robot simulation project 

FOR PROJECT UPDATE 2:
Download ECE470_update_2.ttt for the CoppeliaSim scene, and just press play to start the scene

customizableTable script:
Spawns the blocks that the UR3 arm is to pick up, the size and shape of the object can be adjusted in this script if desired

customizableConveyor script:
Stops the conveyor belt if an object is detected at the proximity sensor at the end of the conveyor belt

UR3 script:
Has the arm use forward kinematics to move to certain locations within the scene as well as open and close the gripper in order to transport the block from the primary conveyor belt to the secondary conveyor belt. If different locations are desired, the joint angles can be adjusted in this script through the targetPos# variables

ConveyorBelt2 script:
Turns the conveyor belt on until an object is not detected at the beginning of the conveyor belt. This is to make space for multiple blocks as they are placed in sequence upon the conveyor belt once this part of the project is reached.

update_2.py script:
Uses matrix exponentials as in Lab 4 to calculate the position and orientation of the end effector. A beta variable is used to translate between mm and the units used in CoppeliaSim. This script works for when the arm has all 0's for joint angles as its initial orientation (as is at the beginning of the scene).  The joint angles of the desired end orientation can be changed in the script in the "theta" variable. The skew_sym function takes in the content of a screw axis (in the form of an omega vector and a v vector) and returns a 4x4 skew-symmetric form matrix. The Get_T() function returns the 4x4 transformation matrix for the end-effector. Just run "update_2.py" or "python update_2.py" at the correct directory to run this script.
