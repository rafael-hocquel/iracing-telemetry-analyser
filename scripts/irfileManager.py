# IMPORTS
import shutil
from pathlib import Path
import sys
from api.objects.IRFile import IRFile

# PATHS
ROOT       = Path(__file__).resolve().parent.parent
FRONT      = ROOT  / "front"
APIFOLDER  = ROOT  / "api"
DATAFOLDER = APIFOLDER / "data-folder"
IBTFOLDER  = DATAFOLDER / "ibt-files"
CSVFOLDER  = DATAFOLDER / "csv-files"


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
def convertIBT2CSV(IRFile: IRFile):
    IBTpath = IBTFOLDER / IRFile.session_name

    if not IBTpath.is_file():
        sys.exit(f"Unable to find the \"{IBTpath}\" ibt file")

# convert to parquet