from flask import Flask
import socket
import multiprocessing
from psutil import virtual_memory

app = Flask(__name__)
@app.route("/status")

def main():
        mem = str(virtual_memory())
        myhost=socket.gethostname()
        hostip = socket.gethostbyname(myhost)
        cpus=str(multiprocessing.cpu_count())
        info="Hostname :" + myhost + "<br>"
        info=info+"IP_Address : " + hostip + "<br>"
        info=info+"CPUs : " + cpus + "<br>"
        info=info+"Memory : " + mem + "<br>"
        return info

if __name__ == "__main__":
    app.run(debug=True, port=8080)
