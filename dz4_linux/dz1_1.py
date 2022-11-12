import random
import subprocess
from datetime import datetime
from calendar import monthrange
import os

subprocess.call("whoami")
subprocess.call("pwd")
subprocess.call(["mkdir", "dz1"])
month_today = datetime.now().month
year_today = datetime.now().year
days_count = monthrange(year_today, month_today)[1]

os.chdir("dz1")
for day in range(1, days_count + 1):
    subprocess.call(["touch", f"{day}-{month_today}-{year_today}.log"])
os.chdir("..")

subprocess.call(["sudo", "chown", "root:root", "dr1"])

os.chdir("dz1")
month_days = [i for i in range(1, days_count + 1)]
for _ in range(5):
    rm_day = random.choices(month_days)
    month_days.remove(rm_day[0])
    subprocess.call(["rm", f"{rm_day[0]}-{month_today}-{year_today}.log"])
