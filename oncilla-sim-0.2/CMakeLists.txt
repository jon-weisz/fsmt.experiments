### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(fsmt-expeiments-oncilla-sim-0.2)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: "${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/tools/plot-sine.sh" DESTINATION ${PREFIX}/share/fsmt-experiments/oncilla-sim-0.2/tools/)
INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/tools/grapher-sine.py" DESTINATION ${PREFIX}/share/fsmt-experiments/oncilla-sim-0.2/tools/)
