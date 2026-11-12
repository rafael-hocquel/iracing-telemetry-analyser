import socket
import webbrowser
from pathlib import Path
import sys
import shutil
import subprocess

target = "localhost"
path = Path(__file__).resolve().parent.parent / "api"
port = 8000

def getURL(adrOnly = False):
    if adrOnly:
        return "127.0.0.1"
    return "http://127.0.0.1:" + str(port)

# FIND OPEN PORT
def findOpenPort():
    global port
    def isPortOpen(port: int):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        return result != 0

    while not isPortOpen(port) and port < 9000:
        port+=1

    return isPortOpen(port)

def runFastAPI():
    uv = shutil.which("uv")
    fastAPI = shutil.which("fastapi")
    if uv is None:
        sys.exit("\"uv\" not found")
    if fastAPI is None:
        sys.exit("\"fastapi\" not found")

    try:
        subprocess.call(uv + " run " + fastAPI + " run --host " + getURL(True) + " --port " + str(port) + " &", cwd=path, shell=True)
    except subprocess.CalledProcessError:
        sys.exit("An error occured while launching the fastAPI server")

def openApp():
    webbrowser.open(getURL())

if __name__ == "__main__":
    if not findOpenPort():
        sys.exit("Unable to find an unoccupied port, try restarting your machine or increasing port-range")

    runFastAPI()
    openApp()