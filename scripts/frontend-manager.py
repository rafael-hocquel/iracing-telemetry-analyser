# IMPORTS
import sys
import shutil
import subprocess
from pathlib import Path

# PATHS
ROOT         = Path(__file__).resolve().parent.parent
FRONT        = ROOT / "front"
OUTFOLDER    = FRONT / "out"
NEXTFOLDER   = FRONT / ".next"
STATICFOLDER = ROOT / "api" / "static"
APIFOLDER    = ROOT / "api"

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

    try:
        shutil.move(OUTFOLDER, STATICFOLDER)
    except FileNotFoundError:
        sys.exit(f"{OUTFOLDER} path was not found")
    except OSError:
        sys.exit(f"Unable to move {OUTFOLDER} to {APIFOLDER}. Check permissions for both paths")


# Import-run guard
if __name__ == "__main__":
    checkProjectIntegrity()
    buildFront()
    setupOUTFolder()