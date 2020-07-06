#include "ros/ros.h"
#include "std_msgs/Empty.h"

int main(int argc, char **argv){

ros::init(argc, argv, "takeoff");
ros::NodeHandle n;
std_msgs::Empty myMsg;
ros::Publisher takeOff=n.advertise<std_msgs::Empty>("/new/takeoff",1, true);
takeOff.publish(myMsg);
ros::spinOnce();

}
