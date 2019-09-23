from gpiozero import Motor, LED, DistanceSensor #import the gpiozero library and Motor, LED and DistanceSensor classes
from time import sleep							#import the time library and sleep class

driverMotor = Motor(forward=25, backward=8)		#set the driver motor to GPIO 25 and 8
steeringMotor = Motor(forward=14, backward=15)	#set the steering motor to GPIO 14 and 15 (forward == right; backward == left)
sensor = DistanceSensor(22, 27)					#set the distance sensor trigger and echo pins to 22 and 27
threshold = 20									#set the distance threshold to 20 cm
front = LED(20)									#set the front LED to GPIO 20
back = LED(21)									#set the back LED to GPIO 21


while True:

	#if current distance is below the threshold, drive back for 2 seconds then turn right
	if sensor.distance * 100 < threshold:
		driverMotor.stop()
		sleep(1)
		front.off()
		back.on()
		driverMotor.backward()
		sleep(2)
		steeringMotor.forward()
		sleep(4)
		steeringMotor.stop()
		back.off()
	#otherwise, keep on driving forward
	else:
		front.on()
		driverMotor.forward()