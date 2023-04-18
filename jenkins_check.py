from subprocess import Popen
from signal import SIGTERM
from time import time, sleep
from os import kill
import sys

# Define the command to run and its arguments
command = ['python3', 'telegram_bot_videocactus.py']

# Define the timeout in seconds
timeout = 10

# Start the subprocess and get its PID
process = Popen(command)

# Wait for the subprocess to complete or for the timeout to expire
start_time = time()
while process.poll() is None and time() - start_time < timeout:
    sleep(0.1)

# If the subprocess is still running, terminate it
if process.poll() is None:
    kill(process.pid, SIGTERM)

if process.returncode != 0:
    print(f"Script failed with error code {process.returncode}")
    sys.exit(1)