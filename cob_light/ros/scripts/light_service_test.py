#!/usr/bin/env python

import rospy
import actionlib
import random

from cob_light.msg import *

from cob_light.srv import SetLightMode
from cob_light.srv import SetLightModeRequest
from cob_light.srv import SetLightModeResponse

from std_msgs.msg import ColorRGBA

class ActionTestScript(object):
    def __init__(self):
        self.executeMode(0)

    def executeMode(self, event):
        rospy.loginfo("setting service mode")
        mode = self.getLightMode(random.randint(0,14))

        srv_light = rospy.ServiceProxy('/light_torso/set_light', SetLightMode)
        srv_light.call(mode)

        duration = random.uniform(0, 0.5)
        self.timer = rospy.Timer(rospy.Duration(duration), self.executeMode, True)

    def getLightMode(self, mode):
        req = SetLightModeRequest()
        req.mode.priority = 4

        if mode == 0:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 2
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(1.0,1.0,1.0,1.0))

        elif mode == 1:
            req.mode.mode=LightModes.FLASH
            req.mode.frequency = 2
            req.mode.pulses = 3
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(1.0,1.0,1.0,1.0))

        elif mode == 2:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.4
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(170.0/255.0, 250.0/255.0, 70.0/255.0, 1.0))

        elif mode == 3:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(70.0/255.0, 140.0/255.0, 250.0/255.0, 1.0))

        elif mode == 4:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(240.0/255.0, 250.0/255.0, 70.0/255.0, 1.0))

        elif mode == 5:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(70.0/255.0, 240.0/255.0, 250.0/255.0, 1.0))

        elif mode == 6: #static yellow black - barrier tape
            yellow = ColorRGBA(70.0/255.0, 240.0/255.0, 250.0/255.0, 1.0)
            black = ColorRGBA()
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            #58 leds
            num_segs = 6
            iterations = int(num_segs/2)
            seg_div = int(58/num_segs)
            for i in range(0, iterations):
                for j in range (0, seg_div):
                    req.mode.colors.append(yellow)
                for j in range (0, seg_div):
                    req.mode.colors.append(black)

        elif mode == 7:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(250.0/255.0, 70.0/255.0, 70.0/255.0, 1.0))

        elif mode == 8:
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.3
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(230.0/255.0, 250.0/255.0, 250.0/255.0, 1.0))

        elif mode == 9:
            req.mode.mode=LightModes.FADE_COLOR
            req.mode.frequency = 0.5
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(1,1,1,1))

        elif mode == 10:
            req.mode.mode=LightModes.FLASH
            req.mode.frequency = 4
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(230.0/255.0, 250.0/255.0, 250.0/255.0, 1.0))

        elif mode == 11:
            req.mode.mode=LightModes.STATIC
            req.mode.frequency = 1
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(150.0/255.0, 120.0/255.0, 255.0/255.0, 1.0))

        elif mode == 12:
            req.mode.mode=LightModes.STATIC
            req.mode.frequency = 1
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(255.0/255.0, 95.0/255.0, 1.0/255.0, 1.0))

        elif mode == 13: #breath fast in red (error)
            req.mode.mode=LightModes.BREATH
            req.mode.frequency = 0.8
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(1.0, 0.0, 0.0, 1.0))

        elif mode == 14: #breath fast in red (error)
            req.mode.mode=LightModes.XMAS
            req.mode.frequency = 0.8
            req.mode.pulses = 0
            req.mode.timeout = 0
            req.mode.colors.append(ColorRGBA(1.0, 0.0, 0.0, 1.0))

        return req


if __name__ == '__main__':
  rospy.init_node('light_service_test')
  ActionTestScript()
  rospy.spin()
