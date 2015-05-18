### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(icub-humanoids)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/cca-lwr-testing-nightly.ini" DESTINATION ${PREFIX}/etc/fsmt-experiments/cca-lwr-testing-nightly/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/cca-lwr-testing-nightly.scxml" DESTINATION ${PREFIX}/etc/fsmt-experiments/cca-lwr-testing-nightly/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/cca_lwr_controller_script" DESTINATION ${PREFIX}/bin/cca_lwr_controller_script)