
import RPi.GPIO as GPIO
import time
GPIO_PWM_0 = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PWM_0, GPIO.OUT)
#GPIO.PWM(GPIO_PWM_0, 50).start(70)

for i in range(1,100):
    GPIO.PWM(GPIO_PWM_0, 50).start(i)
    time.sleep(0.1)
    
    
