from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary storage for job postings
jobs_db = []

class Job(BaseModel):
    company_name: str
    job_title: str
    industry: str
    job_description: str
    experience: str
    package_upto: str
    skills: List[str]
    location: str
    job_type: str
    email: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/post-job/")
def post_job(job: Job):
    jobs_db.append(job)
    return {"message": "Job posted successfully"}

@app.get("/jobs/")
def get_jobs():
    return jobs_db

