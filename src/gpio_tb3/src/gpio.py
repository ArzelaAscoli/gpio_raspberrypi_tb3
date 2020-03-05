#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
import time
import json

from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray


def _gpio_callback(msg):

    gpio_dict = json.loads(msg.data)
    
    pin = gpio_dict['pin']
    value = gpio_dict['value']
    
    if pin == 0:
        GPIO.cleanp()
        rospy.loginfo("GPIO all reset")
   
    elif value == 1:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        rospy.loginfo("pin:" + str(pin) + " High")
    
    elif value == 0:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        rospy.loginfo("pin:" + str(pin) + " Low")
    
    else:
        rospy.loginfo("not str(0) not str(1)")


if __name__ == '__main__':

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    # set up GPIO output channel, we set GPIO4 (Pin 7) to OUTPUT
    # GPIO.setup(7, GPIO.OUT)

    try:
        rospy.init_node('GPIO_controller_generalplus', anonymous=True)
        rospy.Subscriber("/gpio_tb3", String, _gpio_callback)
        rospy.spin()

    except rospy.ROSInterruptException:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

