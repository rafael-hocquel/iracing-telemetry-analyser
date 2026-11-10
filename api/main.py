from fastapi import FastAPI

app = FastAPI()


def main():
    print("--- iracing-telemetry-analyser ---")

@app.get("/api/health")
def read_root():
    return {"status": "healthy", "status_code": 200, "checks": {"fastAPI": "running"}}


if __name__ == "__main__":
    main()
