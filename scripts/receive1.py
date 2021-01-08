#!/usr/bin/env python3
#SPDX-License-Identifier:BSD 3-Clause
#Copyright (C) 2020 Tsubasa Ito. All rights reserved.
import rospy
from std_msgs.msg import String

def cb(message):
    rospy.loginfo(message.data)

if __name__ == '__main__':
    rospy.init_node('receive1')
    sub = rospy.Subscriber('talker', String, cb)
    rospy.spin()
