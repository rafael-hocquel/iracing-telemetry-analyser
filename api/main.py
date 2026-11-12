from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Allowed Origins
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
    print("--- iracing-telemetry-analyser ---")

@app.get("/api/health")
def read_root():
    return {"status": "healthy", "checks": {"fastAPI": "running"}}


if __name__ == "__main__":
    main()
