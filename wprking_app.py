from flask import Flask
app = Flask(__name__)
@app.route("/status")

def main():
        return "Hostname :"

import socket
import multiprocessing


myhost=socket.gethostname()
hostip = socket.gethostbyname(myhost)
cpus=multiprocessing.cpu_count()
print("HostName : " , myhost)
print("IP Address : " , hostip)
print("Memory : " , "a sure it will be grand dont worry")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
