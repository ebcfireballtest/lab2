cmake_minimum_required(VERSION 3.0.2)
project(turtle_control)

# These must match the <build_depend> entries in package.xml.
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  duckietown_msgs
  turtlesim
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs geometry_msgs duckietown_msgs turtlesim
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Param files, so $(find turtle_control)/config/... resolves for roslaunch.
install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)
