import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
in1=17
in2=27
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
p3=4
GPIO.setup(p3, GPIO.OUT)
p1=20
GPIO.setup(p1, GPIO.OUT)
p2=21
GPIO.setup(p2, GPIO.OUT)

#Callback
def myCallback(pin):
    if(pin==17):
        pwm=GPIO.PWM(p1, 100)
        pwm.start(0)
        for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            sleep(.01)
            if dc==100:
                dc=0
                for dc in range(101):
                    pwm.ChangeDutyCycle(100-dc)
                    sleep(.01)
    if(pin==27):
        pwm=GPIO.PWM(p2, 100)
        pwm.start(0)
        for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            sleep(.01)
            if dc==100:
                dc=0
                for dc in range(101):
                    pwm.ChangeDutyCycle(100-dc)
                    sleep(.01)

GPIO.add_event_detect(in1, GPIO.RISING, callback=myCallback, bouncetime=100)
GPIO.add_event_detect(in2, GPIO.RISING, callback=myCallback, bouncetime=100)

try:
    while 1:
            GPIO.output(p3,0)
            sleep(0.5)
            GPIO.output(p3,1)
            sleep(0.5)
except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()