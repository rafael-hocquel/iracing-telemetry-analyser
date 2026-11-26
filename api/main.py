# IMPORTS
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from .objects.IRFile import IRFile

STATICFOLDER = Path(__file__).resolve().parent / "static" / "index.html"
app = FastAPI()

# API Health
@app.get("/api/health")
def health_check():
    return {"status": "healthy", "checks": {"fastAPI": "running"}}

# Upload race-data file
# @app.post("/upload")
# async def manage_datafile(IRFile: IRFile):
    
    


# Keep at the end of the files, otherwises api routes are served as static front files
if STATICFOLDER.is_file():
    app.mount("/", StaticFiles(directory="static", html=True))
else:
    @app.get("/", response_class=HTMLResponse)
    def frontNotBuilt():
        return "<h1>Unable to get the front-end, run frontend-manager.py and try again</h1>"


def main():
    print("--- iracing-telemetry-analyser ---")

if __name__ == "__main__":
    main()
