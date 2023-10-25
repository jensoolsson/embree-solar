## Copyright 2009-2021 Intel Corporation
## SPDX-License-Identifier: Apache-2.0

CMAKE_MINIMUM_REQUIRED(VERSION 3.2.0)

PROJECT(solar)

SET(CMAKE_CXX_STANDARD 11)
FIND_PACKAGE(embree REQUIRED)

ADD_EXECUTABLE(embree_solar main.cpp embree_solar.cpp)
TARGET_LINK_LIBRARIES(embree_solar embree)

