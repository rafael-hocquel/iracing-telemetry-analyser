############################################################
############################################################
## This script searches for a free port, runs fastAPI in  ##
## the open-port and launches the app (when ready) in the ##
## user's default browser. Closes properly with Ctrl + C  ##
############################################################
############################################################

# IMPORTS
import socket
import webbrowser
from pathlib import Path
import sys
import shutil
import subprocess
from time import sleep
from frontendManager import prepareFrontend

# PATHS
APIFOLDER = Path(__file__).resolve().parent.parent / "api"
port      = 8000

# Build and move the frontend (out/) to api/static folder
prepareFrontend()

# Returns the url of the app (address only omits the protocol and port)
def getURL(adrOnly = False):
    if adrOnly:
        return "127.0.0.1"
    return "http://127.0.0.1:" + str(port)

# FIND OPEN PORT
def isPortOpen(port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex(("localhost", port))
    return result != 0

# Scans ports from {port} to 8999 and returns the first one not in use
def findOpenPort():
    global port

    while not isPortOpen(port) and port < 9000:
        port+=1

    return isPortOpen(port)


fastAPIProcess = None
def runFastAPI():
    global fastAPIProcess

    # Get "uv" path
    uv = shutil.which("uv")
    if uv is None:
        sys.exit("\"uv\" not found")

    # TODO : check that dependencies are installed
    # fastAPI = shutil.which("fastapi")
    # if fastAPI is None:
    # sys.exit("\"fastapi\" not found")

    # Start fastAPI process
    fastAPIProcess = subprocess.Popen([uv, "run", "fastapi", "run", "--host", getURL(True), "--port", str(port)], cwd=APIFOLDER)

# Open the app in the default browser
def openApp():
    webbrowser.open(getURL())


if __name__ == "__main__":

    # Returns an error if no available port is found
    if not findOpenPort():
        sys.exit("Unable to find an unoccupied port, try restarting your machine or increasing port-range")

    # Starts the fastAPI process
    runFastAPI()

    # Waits for fastAPI to be ready then launches the app in the default browser
    while isPortOpen(port):
        print("Waiting for app to launch, retrying in a second...")
        sleep(1)    
    openApp()

    # Keeps the program running until stopped with Ctrl+C, then terminates the fastAPI process and quits
    try:
        fastAPIProcess.wait()
    except KeyboardInterrupt:
        fastAPIProcess.terminate()
        print("Process terminated successfully")