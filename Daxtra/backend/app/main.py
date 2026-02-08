from fastapi import FastAPI
from app.routes.resume import resume_router
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(title="AI resume Screening System")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(resume_router)

@app.get("/")

def root():
    return {"message":"Backend is running"}


