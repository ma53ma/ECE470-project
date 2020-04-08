# ECE470-project
Robot simulation project 

FOR PROJECT UPDATE 3:
Download ECE470_project_update_3.ttt for the CoppeliaSim scene, and just press play to start the scene

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ECE470_update_3.ttt 

UR5 script:
Wait until an object is available to pick up, and then have the arm follow the path passed to it from the customizableConveyor script and then return to the original pose of the arm.

ConveyorBelt script:
Set initial parameters and initialize paths. Then, wait until the proximity sensor detects an object, and if this object is to be moved, determine which conveyor belt it should be moved to and change the path of the arm accordingly. In the meantime, delete objects that are detected by the proximity sensor and not to be moved, and spawn objects at the other end of the conveyor belt.

ConveyorBelt2 script:
If the proximity sensor by the depositing area for objects detects an object, turn the conveyor belt to move the object away until it can no longer be detected. If there is no object detected, turn the conveyor belt.

ConveyorBelt3 script:
If the proximity sensor by the depositing area for objects detects an object, turn the conveyor belt to move the object away until it can no longer be detected. If there is no object detected, turn the conveyor belt.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
