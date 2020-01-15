# Omron TM ROS
### Requirements
1. Ubuntu 18.04
2. ROS Melodic
3. Modbus enabled in TM Flow settings 
4. pymodbus python module. To install, run in terminal:
```
pip install  -U pymodbus
```
### Usage
```
roslaunch tm_utils tm_utils.launch ip:=<robot ip address>
```
```
rosrun tm_motion ......................
```
