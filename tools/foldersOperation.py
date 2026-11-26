from pathlib import Path
import shutil
import sys

def moveFolderOrFile(sourcePath: Path, destPath: Path):
    try:
        shutil.move(sourcePath, destPath)
    except FileNotFoundError:
        sys.exit(f"{sourcePath} path was not found")
    except OSError:
        sys.exit(f"Unable to move {sourcePath} to {destPath}. Check permissions for both paths")