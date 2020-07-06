#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Range

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def sub_move():

    rospy.init_node('sub_move', anonymous=True)
    rospy.Subscriber('distance', Twist, callback)
    rospy.Subscriber('drone/sonar', Range, callback)
   

    rospy.spin()

if __name__ == '__main__':
    sub_move()

