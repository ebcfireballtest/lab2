#!/usr/bin/env python3
"""
ECEN 433 - Lab 2, Parts III and IV
==================================

Report which way the turtle is currently facing.

Part III: subscribe to `turtle1/pose` and publish a std_msgs/String on
`turtle1/direction` saying whether the turtle is heading up, down, left,
or right.

Part IV: publish at a rate controlled by the ROS parameter
`/direction_pub_rate` (in Hz), and make it respond when someone runs

    rosparam set /direction_pub_rate 5

while your node is already running.
"""

import rospy
# You need to import the message types you use as Python classes
from std_msgs.msg import String
from turtlesim.msg import Pose

DEFAULT_PUB_RATE_HZ = 1.0

class DirectionNode:
    def __init__(self):
        rospy.init_node("direction_node")

        # Create the subscriber on the turtle1/pose with msg type Pose.
        # The pose_callback function is called every time a new message arrives.
        self.sub = rospy.Subscriber("turtle1/pose", Pose, self.pose_callback)

        # TODO setup the direction publisher 

        rospy.loginfo("direction_node started")

    def pose_callback(self, msg):
        """Called by ROS every time a new Pose arrives. Keep this fast."""
        # TODO store msg so the main loop can use it.
        
        pass

    def heading_to_direction(self, theta):
        """Convert a heading in radians into one of: up, down, left, right."""
        # ------------------------------------------------------------------
        # TODO (Part III): map theta onto the four compass directions.
        #
        # math.pi is useful here (remember to import math).
        # ------------------------------------------------------------------
        return "unknown"

    def run(self):
        while not rospy.is_shutdown():

            # --------------------------------------------------------------
            # TODO (Part IV): read the /direction_pub_rate parameter HERE,
            # inside the loop - not once up in __init__.
            #
            # ROS does not notify a node when a parameter changes. If you read
            # it only at startup, `rosparam set` will appear to do nothing and
            # you will lose points. Reading it is what makes the change 
            # take effect immediately. 
            # 
            #   rate_hz = rospy.get_param("/direction_pub_rate", DEFAULT_PUB_RATE_HZ)
            # 
            # However, reading it every iteration can significantly slow down your
            # loop. This may not affect you now, but it will in future labs.
            # Try and figure out a way to read it at a specified rate.
            # --------------------------------------------------------------
            rate_hz = 

            if self.latest_pose is not None:

                # TODO: convert the latest pose into a direction string
                direction = self.heading_to_direction( )

                # TODO (Part III): publish `direction` as a String message.
                rospy.loginfo("facing %s", direction)

            # Build the Rate object from the value we just read
            rospy.Rate(rate_hz).sleep()


if __name__ == "__main__":
    try:
        DirectionNode().run()
    except rospy.ROSInterruptException:
        pass
