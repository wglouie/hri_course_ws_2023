cmake_minimum_required(VERSION 2.8.3)

project(example_package)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
catkin_package()

catkin_install_python(PROGRAMS scripts/topic_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
