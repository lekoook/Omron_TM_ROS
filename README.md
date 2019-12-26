# Omron TM ROS
### Requirements
1. Ubuntu 18.04
2. ROS Melodic
3. pymodbus python module. To install, run in terminal:
```
pip install  -U pymodbus
```
### Usage
```
roslaunch tm_utils tm_utils.launch ip:=<robot ip address>
```
```
rosrun tm_motion move_joint.py <ip address> <j1> <j2> <j3> <j4> <j5> <j6>
```
