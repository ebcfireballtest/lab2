#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------

# Launches turtlesim plus your Lab 2 nodes.
# Run it from outside the container with:
#
#     dts devel run -X -L square
#
dt-exec roslaunch turtle_control turtle_control.launch

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
