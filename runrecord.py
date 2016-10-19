import subprocess
import time

subprocess.Popen(["rec","pytest.wav","silence","1","5","2%"])

time.sleep(10)

subprocess.Popen(["pkill","rec"])
