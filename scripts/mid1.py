#!/usr/bin/env python3
#SPDX-License-Identifier:GPL-3.0
#Copyright (C) 2020 Tsubasa Ito.  All rights reserved.
import rospy
import random
from std_msgs.msg import String

n = 0
display = 0
time = 0
rand = 0
def cb(message):
    global n
    n = message.data

pub = rospy.Publisher('talker', String, queue_size=1)

if __name__ == '__main__':
    rospy.init_node('mid1')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        sub = rospy.Subscriber('chatter', String, cb)

        if n == "Hello,Noko":
            display = "Hello,human.:)"
            n = 0
            pub.publish(display)
            time += 1
            print(time)
        elif n == "See You, Noko":
            display = "see you ;)"
            n = 0
            pub.publish(display)
            time += 1
            print(time)
        elif n == "How about you?":
            rand = random.randint(0,2)

            if rand == 0:
            display = "I'm fine. Thank you!"
            n = 0
            pub.publish(display)
            time += 1
            print(time)

            else if rand == 1:
            display = "I'm so sad... :( but,Thank you."
            n = 0
            pub.publish(display)
            time += 1
            print(time)

            else if rand == 2:
                display = "I'm so happy with you.:)"
            n = 0
            pub.publish(display)
            time += 1
            print(time)

        elif n == 0:
            display = "…what?"
        else:
            display = "hello world"
            n = 0
            pub.publish(display)
            time += 1
            print(time)
        rate.sleep()
