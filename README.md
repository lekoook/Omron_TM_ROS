# Omron TM ROS
### Requirements
1. Ubuntu 18.04
2. ROS Melodic
3. Modbus enabled in TM Flow settings (might need to turn it off and on).
4. Set computer ethernet ipv4 address as 192.168.1.100 and subnet 255.255.255.0 in ubuntu settings.
5. pymodbus python module. To install, run in terminal:
```
pip install  -U pymodbus
```
6. Import ROS_Vision_Pick_Place program (TM_Export folder is included in the root of this workspace) and it has to be set as the current project in TM Flow.

### Usage
For vision pick and place:
```
roslaunch tm_motion tm_motion.launch ip:=<robot ip address>
```
```
rosrun tm_motion vision_pick_place_client.py
```
