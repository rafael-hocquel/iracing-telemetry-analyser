###########################################################
###########################################################
## This script builds the Next.js frontend with a static ##
## export then places the out/ folder into api/static    ##
###########################################################
###########################################################

# IMPORTS
import sys
import shutil
import subprocess
from pathlib import Path

# PATHS
ROOT         = Path(__file__).resolve().parent.parent
FRONT        = ROOT  / "front"
NEXTFOLDER   = FRONT / ".next"
OUTFOLDER    = FRONT / "out"
APIFOLDER    = ROOT  / "api"
STATICFOLDER = ROOT  / "api" / "static"

# CHECK PROJECT INTEGRITY
def checkProjectIntegrity():
    # No /front folder
    if not FRONT.is_dir():
        sys.exit("Unable to find \"front/\" folder, check project tree for issues")

    # If there is no api/ folder
    if not APIFOLDER.is_dir():
        sys.exit("Unable to find \"api/\" folder, check project tree for issues")


# CLEAR CACHES AND BUILD NEXTJS STATIC EXPORT
def buildFront():
    npm = shutil.which("npm")
    # No npm installation
    if npm is None:
        sys.exit("\"npm\" not found")

    # Clear out/ and .next/ folder
    try:
        if OUTFOLDER.is_dir():
            shutil.rmtree(OUTFOLDER)
        
        if NEXTFOLDER.is_dir():
            shutil.rmtree(NEXTFOLDER)
    except OSError:
        sys.exit("Error while removing \"out/\" and \".next\" folder")


    # Build Next.JS static export
    try:
        subprocess.run([npm, "run", "build"], cwd=FRONT, check=True)

    except subprocess.CalledProcessError:
        sys.exit("An error occurred while building the static export of the Next.JS frontend")

    # If Next.JS export succeeded, clear the api/static folder
    try:
        if STATICFOLDER.is_dir():
            shutil.rmtree(STATICFOLDER)
    except OSError:
        sys.exit("Error while removing \"api/static/\" folder")


# MOVE front/out TO api/static
def setupOUTFolder():
    # If there is no out/ folder
    if not OUTFOLDER.is_dir():
        sys.exit("Unable to find \"front/out\" folder, check project tree for issues")

    # Move the Next.js out/ folder to the api/static folder
    try:
        shutil.move(OUTFOLDER, STATICFOLDER)
    except FileNotFoundError:
        sys.exit(f"{OUTFOLDER} path was not found")
    except OSError:
        sys.exit(f"Unable to move {OUTFOLDER} to {APIFOLDER}. Check permissions for both paths")

    # Check that the api/static folder exists after move 
    if not STATICFOLDER.is_dir():
        sys.exit("Error while setting up the frontend at api/static/")


# Main function that checks if the project is ready for frontend build,
# builds the fronts and move the out/ folder at the right place for fastAPI
def prepareFrontend():
    checkProjectIntegrity()
    buildFront()
    setupOUTFolder()

# Guard to prevent execution at import time
if __name__ == "__main__":
    prepareFrontend()
