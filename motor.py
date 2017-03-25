import RPi.GPIO as GPIO
import time

class motor(object):

	def __init__(self):

		#to avoid warnings during successive runs
		GPIO.setwarnings(False)

		#set GPIO mode to BOARD
		GPIo.setmode(GPIO.BOARD)

		#designate each pin to the corresponding motor
		self.thrust_pin_1 = 16
		self.thrust_pin_2 = 13
		self.thrust_enable = 18
		self.turn_pin_1 = 11
		self.turn_pin_2 = 12
		self.turn_enable = 15

		#define mode for each of the pins
		self.GPIO.setup(thrust_pin_1, GPIO.OUT)
		self.GPIO.setup(thrust_pin_2, GPIO.OUT)
		self.GPIO.setup(thrust_enable, GPIO.OUT)
		self.GPIO.setup(turn_pin_1, GPIO.OUT)
		self.GPIO.setup(turn_pin_2, GPIO.OUT)
		self.GPIO.setup(turn_enable, GPIO.OUT)

	def enable_motors(self):
		GPIO.output(self.thrust_enable, GPIO.HIGH)
		GPIO.output(self.turn_enable, GPIO.HIGH)

	def disable_motors(self):
		GPIO.output(self.thrust_enable, GPIO.LOW)
		GPIO.output(self.turn_enable, GPIO.LOW)

	def move_forward(self):
		GPIO.output(self.thrust_pin_1, GPIO.HIGH)
		GPIO.output(self.thrust_pin_2, GPIO.LOW)

	def move_backward(self):
		GPIO.output(self.thrust_pin_1, GPIO.LOW)
		GPIO.output(self.thrust_pin_2, GPIO.HIGH)

	def turn_right(self):
		GPIO.output(self.turn_pin_1, GPIO.LOW)
		GPIO.output(self.turn_pin_2, GPIO.HIGH)

	def turn_left(self):
		GPIO.output(self.turn_pin_1, GPIO.HIGH)
		GPIO.output(self.turn_pin_2, GPIO.LOW)
