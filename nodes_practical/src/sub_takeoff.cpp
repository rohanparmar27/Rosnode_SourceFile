
#include "ros/ros.h"
#include "std_msgs/Empty.h"


void chatterCallback(const std_msgs::Empty::ConstPtr& msg)
{
  ROS_INFO("I heard");
}


int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "sub_takeoff");

 
  ros::NodeHandle n;

 
  ros::Subscriber sub = n.subscribe("/new/takeoff", 1, chatterCallback);

  ros::spin();

}

