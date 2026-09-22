#!/usr/bin/env python3
"""
ECEN 433 - Lab 2
================

PROVIDED NODE - read it, but do not edit it.

Your square_node publishes duckietown_msgs/Twist2DStamped, which is the message
a real Duckiebot takes. Turtlesim has never heard of it - turtlesim only
understands geometry_msgs/Twist. This node sits in between and translates:

    turtle1/cmd       (duckietown_msgs/Twist2DStamped)   <- your node publishes here
        |
        |  this node
        v
    turtle1/cmd_vel   (geometry_msgs/Twist)              <- turtlesim listens here

Except that neither of those topic names is written in this file. Look at how
__init__ gets them: they come from ROS PARAMETERS, loaded from
config/turtle_bridge.yaml by the launch file. Read that file - it is two lines,
and it tells you which topic your own node has to publish on.

Three things worth noticing.

1. The parameters are read with a leading "~", which makes them PRIVATE to this
   node - `~input_topic` is really `/turtlesim/turtle_bridge/input_topic`. That
   is what the <rosparam> tag being INSIDE the <node> tag buys you.

2. This is a TYPE conversion, not a UNIT conversion. The numbers pass straight
   through: whatever you put in `v` lands in `linear.x` untouched. Turtlesim
   reads that as "turtle units per second". A Duckiebot would read the same
   number as "metres per second". You can create scale factors for this if you want
"""

import rospy
from geometry_msgs.msg import Twist
from duckietown_msgs.msg import Twist2DStamped

# Defaults, used only if no param file was loaded. The launch file normally
# overrides both of these from config/turtle_bridge.yaml.
INPUT_TOPIC = "turtle1/cmd"
OUTPUT_TOPIC = "turtle1/cmd_vel"


class TurtleBridge:
    def __init__(self):
        rospy.init_node("turtle_bridge")

        # Read once, at startup. A publisher and a subscriber are each built
        # exactly once out of these strings, so there would be nothing for a
        # later value to apply to.
        self.input_topic = rospy.get_param("~input_topic", INPUT_TOPIC)
        self.output_topic = rospy.get_param("~output_topic", OUTPUT_TOPIC)

        self.pub = rospy.Publisher(self.output_topic, Twist, queue_size=10)
        self.sub = rospy.Subscriber(self.input_topic, Twist2DStamped, self.cmd_cb)

        rospy.loginfo("turtle_bridge started: %s -> %s",
                      self.input_topic, self.output_topic)

    def cmd_cb(self, msg):
        """Forward one Twist2DStamped as one Twist. No scaling, no filtering."""
        out = Twist()
        out.linear.x = msg.v
        out.angular.z = msg.omega
        self.pub.publish(out)


if __name__ == "__main__":
    try:
        TurtleBridge()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
