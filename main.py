from fastapi import FastAPI
from app.routes import explain, debug, workflow

app = FastAPI(title="RebootAI - Developer Companion")

app.include_router(explain.router, prefix="/explain", tags=["Explain"])
app.include_router(debug.router, prefix="/debug", tags=["Debug"])
app.include_router(workflow.router, prefix="/workflow", tags=["Workflow"])

@app.get("/")
def root():
    return {"message": "RebootAI Backend Running 🚀"}