# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/xu/anaconda3/lib/python3.11/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/xu/anaconda3/lib/python3.11/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xu/eskf-gps-imu-fusion-main

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xu/eskf-gps-imu-fusion-main/bulid

# Include any dependencies generated for this target.
include CMakeFiles/test_gps.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test_gps.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test_gps.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_gps.dir/flags.make

CMakeFiles/test_gps.dir/test/test_gps.cpp.o: CMakeFiles/test_gps.dir/flags.make
CMakeFiles/test_gps.dir/test/test_gps.cpp.o: /home/xu/eskf-gps-imu-fusion-main/test/test_gps.cpp
CMakeFiles/test_gps.dir/test/test_gps.cpp.o: CMakeFiles/test_gps.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xu/eskf-gps-imu-fusion-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_gps.dir/test/test_gps.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/test_gps.dir/test/test_gps.cpp.o -MF CMakeFiles/test_gps.dir/test/test_gps.cpp.o.d -o CMakeFiles/test_gps.dir/test/test_gps.cpp.o -c /home/xu/eskf-gps-imu-fusion-main/test/test_gps.cpp

CMakeFiles/test_gps.dir/test/test_gps.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_gps.dir/test/test_gps.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xu/eskf-gps-imu-fusion-main/test/test_gps.cpp > CMakeFiles/test_gps.dir/test/test_gps.cpp.i

CMakeFiles/test_gps.dir/test/test_gps.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_gps.dir/test/test_gps.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xu/eskf-gps-imu-fusion-main/test/test_gps.cpp -o CMakeFiles/test_gps.dir/test/test_gps.cpp.s

# Object files for target test_gps
test_gps_OBJECTS = \
"CMakeFiles/test_gps.dir/test/test_gps.cpp.o"

# External object files for target test_gps
test_gps_EXTERNAL_OBJECTS =

test_gps: CMakeFiles/test_gps.dir/test/test_gps.cpp.o
test_gps: CMakeFiles/test_gps.dir/build.make
test_gps: libDEPS.so
test_gps: /usr/lib/x86_64-linux-gnu/libglog.so
test_gps: GeographicLib/liblibGeographiccc.so
test_gps: CMakeFiles/test_gps.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xu/eskf-gps-imu-fusion-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_gps"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_gps.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_gps.dir/build: test_gps
.PHONY : CMakeFiles/test_gps.dir/build

CMakeFiles/test_gps.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_gps.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_gps.dir/clean

CMakeFiles/test_gps.dir/depend:
	cd /home/xu/eskf-gps-imu-fusion-main/bulid && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xu/eskf-gps-imu-fusion-main /home/xu/eskf-gps-imu-fusion-main /home/xu/eskf-gps-imu-fusion-main/bulid /home/xu/eskf-gps-imu-fusion-main/bulid /home/xu/eskf-gps-imu-fusion-main/bulid/CMakeFiles/test_gps.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_gps.dir/depend
