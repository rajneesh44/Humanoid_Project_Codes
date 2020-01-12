import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
mla=23
mlb=36
mra=37
mrb=38

GPIO.setup(mla,GPIO.OUT)
GPIO.setup(mlb,GPIO.OUT)
GPIO.setup(mra,GPIO.OUT)
GPIO.setup(mrb,GPIO.OUT)
sh=6.5
sv=4.25

sleep(0.5)

while 1:
    direction = '0'
    if direction=='0':
        GPIO.output(mla,1)
        GPIO.output(mlb,1)
        GPIO.output(mra,1)
        GPIO.output(mrb,1)
        print("forward")
        sleep(5)
    elif direction=='1':
        GPIO.output(mla,0)
        GPIO.output(mlb,1)
        GPIO.output(mra,1)
        GPIO.output(mrb,0)
        print("left")
    elif direction=='2':
        GPIO.output(mla,1)
        GPIO.output(mlb,0)
        GPIO.output(mra,0)
        GPIO.output(mrb,1)
        print("right")
    elif direction=='3':
        GPIO.output(mla,0)
        GPIO.output(mlb,1)
        GPIO.output(mra,0)
        GPIO.output(mrb,1)
        print("backward")
    else:
        GPIO.output(mla,0)
        GPIO.output(mlb,0)
        GPIO.output(mra,0)
        GPIO.output(mrb,0)
        print("stop")         




