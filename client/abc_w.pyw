import subprocess
import schedule
import time

def job(t):
    subprocess.call(["C:\Python27\pythonw.exe","fullClient.py"])
    return schedule.CancelJob

schedule.every().day.at("15:05").do(job,"done")

while True:
    schedule.run_pending()
time.sleep(1)
