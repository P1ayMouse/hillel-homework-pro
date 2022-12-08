#!/usr/bin/python3

import subprocess

subprocess.call(["cp", "dz1_1.py", "dz1_run.py"])

subprocess.call(["chmod", "u+x", "dz1_run.py"])

subprocess.call(["chmod", "u+rx,g=,o=", "dz1_run.py"])

subprocess.call("./dz1_run.py", shell=True)
