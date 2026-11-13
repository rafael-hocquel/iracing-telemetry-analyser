import socket
import webbrowser
from pathlib import Path
import sys
import shutil
import subprocess
import freeport
import atexit
from time import sleep

target    = "localhost"
path      = Path(__file__).resolve().parent.parent / "api"
port      = 8000

def getURL(adrOnly = False):
    if adrOnly:
        return "127.0.0.1"
    return "http://127.0.0.1:" + str(port)

# FIND OPEN PORT
def isPortOpen(port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    return result != 0

def findOpenPort():
    global port

    while not isPortOpen(port) and port < 9000:
        port+=1

    return isPortOpen(port)


fastAPIProcess = None
def runFastAPI():
    global fastAPIProcess
    uv = shutil.which("uv")
    # TODO : check that dependencies are installed
    # fastAPI = shutil.which("fastapi")
    if uv is None:
        sys.exit("\"uv\" not found")
    # if fastAPI is None:
    #     sys.exit("\"fastapi\" not found")

    fastAPIProcess = subprocess.Popen([uv, "run", "fastapi", "run", "--host", getURL(True), "--port", str(port)], cwd=path)

def openApp():
    webbrowser.open(getURL())

if __name__ == "__main__":
    if not findOpenPort():
        sys.exit("Unable to find an unoccupied port, try restarting your machine or increasing port-range")
    runFastAPI()

    while isPortOpen(port):
        print("Waiting for app to launch, retrying in a second...")
        sleep(1)    
    openApp()

    try:
        fastAPIProcess.wait()
    except KeyboardInterrupt:
        fastAPIProcess.terminate()
        print("Process terminated successfully")