#!/usr/bin/env python3
#SPDX-License-Identifier:BSD 3-Clause
#Copyright (C) 2020 Tsubasa Ito.  All rights reserved.
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('reply1')
    pub = rospy.Publisher('chatter', String, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hell = input(">")
        pub.publish(hell)
        rate.sleep()
