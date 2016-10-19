import subprocess
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

#subprocess.Popen(["rec","pytest.wav","silence","1","5","2%"])
#time.sleep(10)
#subprocess.Popen(["pkill","rec"])

recording = False

try:
    while True:
        if (GPIO.input(12)):
            print("BUTTON IS ON")
            subprocess.Popen(["rec","pytest.wav","silence","1","5","2%"])
            recording = True
        else:
            if (recording):
                subprocess.Popen(["pkill","rec"])
                recording = False
except KeyboardInterrupt:
    pass
