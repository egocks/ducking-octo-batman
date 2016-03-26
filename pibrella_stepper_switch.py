# controlling the stepper motor using Pibrella
# a variation on motor_switch.py

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

def button_pressed(pin):
	if pin.read() == 1:
		forward(int(2) / 1000.0, int(100))	
		print("moved forward")
	else:
		setStep(0,0,0,0)
		print("stopped")
		time.sleep(0.1)

pibrella.button.pressed(button_pressed)

pibrella.pause()
