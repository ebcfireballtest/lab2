#!/usr/bin/env python3
"""
ECEN 433 - Lab 2, Part II
=========================

Drive the turtlesim turtle in a repeating square.

The message
-----------
You publish duckietown_msgs/Twist2DStamped - the same chassis message you sent
to your Duckiebot's wheels in Lab 1:

    msg.header  standard ROS header
    msg.v       linear speed, forward is positive
    msg.omega   angular speed in radians per second, counter-clockwise positive

That is all a differential-drive robot gives you: how fast to go, and how fast
to spin.

The topic
---------
You do NOT publish on `turtle1/cmd_vel`, even though that is the topic you
found in Part I. Turtlesim cannot read Twist2DStamped, so a provided node -
turtle_bridge.py - listens for it, converts each message to
geometry_msgs/Twist, and republishes it where turtlesim is listening.

Why publish the robot's message into a simulator? Because in Part V you will
point this exact file at your Duckiebot without editing a line of it.
"""

import rospy
from duckietown_msgs.msg import Twist2DStamped

# How often we publish a command, in Hz. Commands need to be
# sent at a continous rate because the turtlesim will timeout
# if it does not receive a command for a few seconds.
PUBLISH_RATE_HZ = 10.0


class SquareNode:
    def __init__(self):
        rospy.init_node("square_node")

        # ------------------------------------------------------------------
        # TODO (Part V): read the topic name, and whatever speed and timing
        # constants you ended up writing for Part II, from ROS parameters
        # instead of hard-coding them. That is what lets you point this same
        # file at your Duckiebot without editing it.
        #
        # turtle_bridge.py already does exactly this - read it and
        # config/turtle_bridge.yaml together for the worked version.
        # ------------------------------------------------------------------

        # Where the commands go. turtle_bridge.py is listening here.
        CMD_TOPIC = "turtle1/cmd"

        # Create the publisher on turtle1/cmd with msg type Twist2DStamped.
        self.pub = rospy.Publisher(CMD_TOPIC, Twist2DStamped, queue_size=10)

        self.rate = rospy.Rate(PUBLISH_RATE_HZ)

        rospy.loginfo("square_node started, publishing to %s", CMD_TOPIC)

    def run(self):

        while not rospy.is_shutdown():
            # This will loop until the node is shutdown (Ctrl-C)

            msg = Twist2DStamped()

            # --------------------------------------------------------------
            # TODO (Part II): make the turtle drive in a repeating square.
            # Do this by filling in msg.v and msg.omega.
            # --------------------------------------------------------------


            # This command uses the publisher method to send out the message
            # It will be sent to the topic defined in the publisher
            self.pub.publish(msg)

            # This will hold the loop for (1/PUBLISH_RATE_HZ) seconds
            self.rate.sleep()


if __name__ == "__main__":
    try:
        SquareNode().run()
    except rospy.ROSInterruptException:
        pass
