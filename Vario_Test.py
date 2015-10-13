# Vario test
import RPi.GPIO as gp
import time
import Adafruit_BMP.BMP085 as BMP085

gp.setmode(GPIO.BOARD)
gp.setup(18, GPIO.OUT)

bmp = BMP085(0x77, 2)
frequencyHertz = 50.
pwm = gp.PWM(18, frequencyHertz)
msPerCycle = 1000 / frequencyHertz

# Left and right positions of the PWM signal
lp = 0.75
rp = 2.5

# Max and Min climb rates
fpm_MAX = 2000.
fpm_MIN = -2000.

# Time delta depends on the conversion time 
# for the BMP180 sensor: 
# Ultra low power mode:  4.5 ms
# Standard mode:         7.5 ms
# High resolution mode: 13.5 ms
# Ultra high res mode:  25.5 ms
# Advanced res mode:    76.5 ms
time_delta = 15

# Parameters of the y-equation
m = (rp - lp) / (fpm_MAX - fpm_MIN)
b = rp - m * (FPM_MAX)

# Constant to convert altitude from m to ft
k = 3.28084

# Determine climb rate
def Fpm(alt1, alt2):
    fpm = (alt1 - alt2) / time_delta
    return fpm

# Determine PWM for the beep
def beep(fpm, y, m, b):
    y = m * fpm + b
    dutyCyclePercentage = y * 100 / msPerCycle
    pwm.start(dutyCyclePercentage)
    time.sleep(time_delta)

# Read the altitude
alt = bmp.readAltitude() * k

while True:
    alt1 = bmp.readAltitude()
    Fpm()
    beep()
    alt2 = alt1


        


     
    