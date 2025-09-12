# init cmake
cmake_minimum_required(VERSION 3.16)
project(engine VERSION 1.0 LANGUAGES CXX)

# set required version
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# get pybind directory
if(DEFINED ENV{VIRTUAL_ENV})
    execute_process(
        COMMAND $ENV{VIRTUAL_ENV}/bin/python -m pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
endif()

# find pybind
find_package(pybind11 REQUIRED CONFIG)

file(GLOB CPP_SOURCES src/cpp/*.cpp)

# create cpp module thats accesible for python
pybind11_add_module(engine
    ${CPP_SOURCES}
    src/bindings/bindings.cpp
)

# include those files
target_include_directories(engine PRIVATE
    src/cpp
    src/bindings
)

# define output directory and force .so suffix
set_target_properties(engine PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/src/py
    SUFFIX ".so"
)
