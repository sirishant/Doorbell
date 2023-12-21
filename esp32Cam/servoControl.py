# Actuate the Servo Motor MG995

import machine
import time

servoPin = 15		# GPIO 15
min_duty = 25.6		# 0 deg
max_duty = 128		# 180 deg
freq = 50

def map(ang):		# Maps a duty value for given Angle
    return int((ang - 0)*(max_duty - min_duty)/(180 - 0) + min_duty)

servo = machine.Pin(servoPin, machine.Pin.OUT)
pwm = machine.PWM(servo)
pwm.duty(0)			# Initial 0 deg
pwm.freq(freq)		# Set freq = 50Hz

def mov(deg):
    for i in range(0, deg+1, 10):	# Move by 10 deg
        pwm.duty(map(i))			# every 5 ms
        time.sleep(.005)
    time.sleep(.25)					# At 180deg, wait 250ms
    for i in range(deg, -1, -10):
        pwm.duty(map(i))			# Return by 10 deg
        time.sleep(.005)			# every 5 ms
    return
