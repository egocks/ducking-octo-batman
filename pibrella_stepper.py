# controlling the stepper motor using Pibrella
# a variation on stepper.py

import pibrella, time

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
	pibrella.output.e.write(w1)
	pibrella.output.f.write(w2)
	pibrella.output.g.write(w3)
	pibrella.output.h.write(w4)

while True:
	delay = raw_input("Delay between steps (milliseconds)?")
	steps = raw_input("How many steps forward?")
	forward(int(delay) / 1000.0, int(steps))
	steps = raw_input("How many steps backwards?")
	backwards(int(delay) / 1000.0, int(steps))

setStep(0,0,0,0)
