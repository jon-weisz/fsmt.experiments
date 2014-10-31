### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(icub-main-nightly)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: "${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/icub-main-nightly-smc.py" DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/icub-main-nightly-smc.ini" DESTINATION ${PREFIX}/etc/fsmt-experiments/icub-main-nightly/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/icub-main-nightly-smc.scxml" DESTINATION ${PREFIX}/etc/fsmt-experiments/icub-main-nightly/)
