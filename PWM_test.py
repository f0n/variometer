# Variometer implementation with the Raspberry PI

# Library to control the pins
import RPi.GPIO as gp

# Library to control time delays
import time

#**** PWM for the buzzer ****
# Based on https://www.youtube.com/watch?v=N5QmZ92uvUo
# Set the GPIO mode
gp.setmode(GPIO.BOARD)

# Set the GPIO pin 18
gp.setup(18, GPIO.OUT)

# Set the frequency
frequencyHertz = 50.
pwm = gp.PWM(11, frequencyHertz)

# Calculate the duty cycle for the specific duration
# Firts, know the pulse time for the position desired
# In this case, 0.75 and 2.5 ms
leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition) / 2. + leftPosition

# This array stores 4 different positions
positionList = [leftPosition, middlePosition, rightPosition, middlePosition]

# We want to know how long we want the pulse in the cycle and how long the cycle is.
# Thus, we can calculate the duty cycle as a percentage
msPerCycle = 1000 / frequencyHertz

# Iterate through the positions 3 times
for i in range(3):
    for position in positionList:
        dutyCyclePercentage = position * 100 / msPerCycle
        print "Position" + str(position)
        print "Duty Cycle" + str(dutyCyclePercentage) + "%"
        print ""
        pwm.start(dutyCyclePercentage)
        time.sleep(.5)

# Done. Terminate signals and relax the motor
pwm.stop()

# Need to do a complete close out of the GPIO stuff. Release the GPIO for other processes
gp.cleanup()