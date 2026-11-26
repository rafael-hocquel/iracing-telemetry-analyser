# IMPORTS
import shutil
import subprocess
from pathlib import Path
import sys
from api.objects.IRFile import IRFile
from tools.foldersOperation import moveFolderOrFile

# PATHS
ROOT         = Path(__file__).resolve().parent.parent
FRONT        = ROOT  / "front"
APIFOLDER    = ROOT  / "api"
OUTPUTFOLDER = ROOT / "tools" / "ibtConversion" 
DATAFOLDER   = ROOT / "data"
IBTFOLDER    = DATAFOLDER / "ibt"
CSVFOLDER    = DATAFOLDER / "csv"


def checkProjectIntegrity():
    # No /front folder
    if not FRONT.is_dir():
        sys.exit("Unable to find \"front/\" folder, check project tree for issues")

    # If there is no api/ folder
    if not APIFOLDER.is_dir():
        sys.exit("Unable to find \"api/\" folder, check project tree for issues")

    # If there is no api/data-files folder
    if not DATAFOLDER.is_dir():
        sys.exit("Unable to find \"api/data-files\" folder, check project tree for issues")

    # If there is no api/data-files folder
    if not IBTFOLDER.is_dir():
        sys.exit("Unable to find \"api/data-files/ibt-files\" folder, check project tree for issues")

    # If there is no api/data-files folder
    if not CSVFOLDER.is_dir():
        sys.exit("Unable to find \"api/data-files/csv-files\" folder, check project tree for issues")

# convert to csv
# Remove = None after proper api implementation
def convertIBT2CSV(IRFile: IRFile = None):
    # TEMPORARY BEFORE PROPER FILE UPLOAD
    IBTpath = IBTFOLDER / "test-lap.ibt"
    # FINAL VERSION -> IBTpath = IBTFOLDER / IRFile.session_name

    NPM = shutil.which("npm")

    # If npm is not installed
    if NPM is None:
        sys.exit("Could not find \"npm\", please install it and try again")

    # If the .ibt file path is incorrect
    if not IBTpath.is_file():
        sys.exit(f"Unable to find the \"{IBTpath}\" ibt file")

    # Convert the .ibt to .csv
    try:
        subprocess.run([NPM, "run", "csv", IBTpath], cwd=OUTPUTFOLDER)
    except subprocess.CalledProcessError:
        sys.exit("An error occured while running the .ibt to .csv script. Try again later.")

    # Move the .csv output to data/csv folder
    # Change file rename when proper api integration is done
    moveFolderOrFile(OUTPUTFOLDER / "output.csv", CSVFOLDER / "test-lap.csv")

convertIBT2CSV()
# convert to parquet