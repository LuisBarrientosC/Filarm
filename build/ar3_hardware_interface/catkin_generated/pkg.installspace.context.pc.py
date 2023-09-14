# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "hardware_interface;controller_manager;roscpp;urdf;joint_limits_interface;ar3_hardware_drivers".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lar3_hardware_interface".split(';') if "-lar3_hardware_interface" != "" else []
PROJECT_NAME = "ar3_hardware_interface"
PROJECT_SPACE_DIR = "/home/yelidi/ar3_ws/install"
PROJECT_VERSION = "0.0.1"
