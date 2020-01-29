# Omron TM ROS
![omron tm robot](http://www.ia.omron.com/Images/l_3739-13-287289-198x198.jpg "omron tm robot")
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

### Compatibility

Tested on TM Flow 1.72 and 1.76

### Installation

This readme assumes that you have installed catkin and sourced your environment. If you installed catkin via apt-get for ROS melodic, your command would look like this:
```
source /opt/ros/melodic/setup.bash
```
Clone the repository into the your home directory:
```
git clone https://github.com/tthmatt/Omron_TM_ROS.git
```
Your workspace hierarchy should look like this:



Use catkin build to compile and make sure to source the workspace:
```
cd ~/Omron_TM_ROS

catkin clean

catkin build

source ~/Omron_TM_ROS/devel/setup.bash
```

### Usage
For vision pick and place:

set robot coordinates to scan tm landmark and offset from tm landmark in launch file. 
For example: <param name="pick_scan_location" value="-326.47,-53.09,646.33,-177.09,-1.64,-90.20" />
Then run in terminal: 
```
roslaunch tm_motion tm_motion.launch ip:=<robot ip address>
```

