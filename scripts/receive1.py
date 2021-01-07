#!/usr/bin/env python3
#SPDX-License-Identifier:GPL-3.0
#Copyright (C) 2020 Tsubasa Ito and Ryuichi Ueda.  All rights reserved.
import rospy
from std_msgs.msg import String

def cb(message):
    rospy.loginfo(message.data)

if __name__ == '__main__':
    rospy.init_node('kaa')
    sub = rospy.Subscriber('kaaer', String, cb)
    rospy.spin()
