#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from sensor_msgs.msg import Range

def move():
  
        
        pub_takeoff = rospy.Publisher("drone/takeoff", Empty, queue_size=1)
        pub_land = rospy.Publisher("drone/land", Empty, queue_size=1)
	pub_sonar = rospy.Publisher("drone/sonar", Range, queue_size=1)
        pub_distance = rospy.Publisher("distance", Twist, queue_size=1)
        pub_reset = rospy.Publisher("drone/reset", Empty, queue_size=10)
        rospy.init_node('move', anonymous=True)
        rate =rospy.Rate(10)
        hover_msg = Twist()
        hover_msg.linear.x = 0
        hover_msg.linear.y = 0
        hover_msg.linear.z = 0
        hover_msg.angular.x = 0
        hover_msg.angular.y = 0
        hover_msg.angular.z = 0
        distance = Range()

       
      
        while not rospy.is_shutdown():
            
            
            pub_takeoff.publish(Empty())
		
            pub_distance.publish(hover_msg)
            pub_sonar.publish(Range())
                    
            print(Range())
            if distance.range == 2:
                pub_distance.publish(hover_msg)
                pub_land.publish(Empty())
            else:
                pub_distance.publish(hover_msg)
            rate.sleep()     

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
