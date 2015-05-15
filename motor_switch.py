# A motion activated stepper motor
# A combination of switches.py and stepper.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def forward(delay, steps):
	for i in range(0, steps):
		setStep(1,0,1,0)
		time.sleep(delay)
		setStep(0,1,1,0)
		time.sleep(delay)
		setStep(0,1,0,1)
		time.sleep(delay)
		setStep(1,0,0,1)
		time.sleep(delay)

def backwards(delay, steps):
	for i in range(0, steps):
		setStep(1,0,0,1)
		time.sleep(delay)
		setStep(0,1,0,1)
		time.sleep(delay)
		setStep(0,1,1,0)
		time.sleep(delay)
		setStep(1,0,1,0)
		time.sleep(delay)

def setStep(w1, w2, w3, w4):
	GPIO.output(coil_A_1_pin, w1)
	GPIO.output(coil_A_2_pin, w2)
	GPIO.output(coil_B_1_pin, w3)
	GPIO.output(coil_B_2_pin, w4)

moved = False
forwarded = False
while True:
	if io.input(pir_pin):
		moved = not moved
	if moved:
		forward(int(2) / 1000.0, int(100))	
	else
		setStep(0,0,0,0)
