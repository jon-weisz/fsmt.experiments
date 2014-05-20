### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(fsmt-experiments-morse-find-human-1.2)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: "${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/hri-morse-find-scenario.py"  DESTINATION  ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/hri-start-waypoint.py"       DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/hri-morse-log-human.py"      DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/hri-start-human-waypoint.py" DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/hri-ros-image-view.py"       DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/hri-morse-find-scenario.ini"   DESTINATION ${PREFIX}/etc/fsmt-experiments/MORSE-find-human-1.2/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/hri-morse-find-scenario.scxml" DESTINATION ${PREFIX}/etc/fsmt-experiments/MORSE-find-human-1.2/)

