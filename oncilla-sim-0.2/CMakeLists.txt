### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(fsmt-expeiments-oncilla-sim-0.2)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/onc-sim0.2-grapher-sine.py" DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/onc-sim0.2-plot-sine.sh" DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/oncilla-sim-0.2-trajactory.ini" DESTINATION ${PREFIX}/etc/fsmt-experiments/onc-sim-0.2-sine/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/oncilla-sim-0.2-trajactory.scxml" DESTINATION ${PREFIX}/etc/fsmt-experiments/onc-sim-0.2-sine/)

