cmake_minimum_required(VERSION 3.4)

set(BINDINGS py_embree_solar)

project(embree_solar)

FIND_PACKAGE(embree REQUIRED)

add_subdirectory(pybind11)


pybind11_add_module(${BINDINGS} embree_solar.cpp)
target_link_libraries(${BINDINGS} PRIVATE embree)

install(TARGETS ${BINDINGS} DESTINATION embree-solar)