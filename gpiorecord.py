import subprocess
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

recording = False

try:
    while True:
        sleep(1)
        if (GPIO.input(12)):
            if (recording == False):
                recording = True
                print("BUTTON IS ON")
                subprocess.Popen(["rec","pytest.wav","silence","1","5","2%"])
        else:
            print("BUTTON IS OFF")
            if (recording):
                subprocess.Popen(["pkill","rec"])
                recording = False
                subprocess.Popen(["aplay","pytest.wav"])
except KeyboardInterrupt:
    GPIO.cleanup()
