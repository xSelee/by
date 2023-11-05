#uptime
from flask import Flask
from threading import Thread
import datetime
import subprocess
from keep_alive import keep_alive

app = Flask(__name__)

@app.route('/')
def main_func():
    
    content = "<p>" + "Online @ " + str(datetime.datetime.now()) + "</p>"
    return "Hey Selee im Alive"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()


subprocess.Popen('python b1.py',shell=True)
subprocess.Popen('python b2.py',shell=True)
subprocess.Popen('python b3.py',shell=True)
subprocess.Popen('python b4.py',shell=True)
subprocess.Popen('python b5.py',shell=True)

keep_alive()
