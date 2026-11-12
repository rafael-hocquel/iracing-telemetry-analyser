from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

def main():
    print("--- iracing-telemetry-analyser ---")

@app.get("/api/health")
def read_root():
    return {"status": "healthy", "checks": {"fastAPI": "running"}}

# Keep at the end of the files, otherwises api routes are served as static front files
app.mount("/", StaticFiles(directory="static", html=True))

if __name__ == "__main__":
    main()
