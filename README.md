# Omron TM ROS
![omron tm robot](http://www.ia.omron.com/Images/l_3739-13-287289-198x198.jpg "omron tm robot")
### Requirements
1. Ubuntu 18.04
2. ROS Melodic
3. Modbus enabled in TM Flow settings (might need to turn it off and on).
4. Set computer ethernet ipv4 address as 192.168.1.100 and subnet 255.255.255.0 in ubuntu settings.
![ipv4 settings](https://user-images.githubusercontent.com/8951670/73414272-40f9ae80-4349-11ea-90aa-3d5ec7d12a5c.png)
5. pymodbus python module. To install, run in terminal:
```
pip install  -U pymodbus
```
6. Import ROS_Vision_Pick_Place program (TM_Export folder is included in the root of this workspace) and it has to be set as the current project in TM Flow.

### TM Flow program explanation 
![tm_ros_program_pic1](https://user-images.githubusercontent.com/8951670/73413992-74880900-4348-11ea-88c0-7152199c0be8.png)

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

Specify robot coordinates to scan tm landmark and offset from tm landmark(refer to image below). Values should be separated by commars without spaces in launch file. 
![tm_landmark_coordinates](https://user-images.githubusercontent.com/8951670/73336836-dba4af80-42ad-11ea-8c8e-25acb1e09006.png)

For example: 

\<param name="pick_scan_location" value="-326.47,-53.09,646.33,-177.09,-1.64,-90.20" />

\<param name="pick_offset" value="100,0,-350" />

Then run in terminal: 
```
roslaunch tm_motion tm_motion.launch ip:=<robot ip address>
```

