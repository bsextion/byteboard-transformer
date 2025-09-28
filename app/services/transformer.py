from app.schemas.job import JobDetailsRequest
from app.schemas.job import JobDetailsResponse 

import spacy


nlp = spacy.load("en_core_web_sm")

skill_keywords = {"python", "node", "react", "reactjs", "ai", "machine learning", "vue", "golang", ".net", "angular", "java", "javascript", "typescript", "git", "spring", "c#", "c++", "fastapi", "docker", "kubernetes", "aws", "sql", "javascript", "html", "css", "tailwind", "ruby", "rails", "php", "laravel", "django", "flask", "tensorflow", "pytorch", "nlp", "data science", "data analysis", "devops", "ci/cd", "rest api", "graphql", "microservices", "agile", "scrum"}
cert_keywords = {"aws certified", "certified kubernetes administrator", "pmp", "cissp", "cisa", "ceh", "compTIA", "bachelor", "master", "phd"}

def transformDescription(jobDetails: list[JobDetailsRequest]) -> dict[str, JobDetailsResponse]:
    response = {}
    print("Transforming job descriptions...")
    for job in jobDetails:
        print(f"Processing job ID: {job.job_id}")
        extractSkillsCerts(job, response)
    return response

def extractSkillsCerts(job: JobDetailsRequest, response: dict[str, JobDetailsResponse]) -> None:
    doc = nlp(job.job_description.strip())
    skills = set()
    certs = set()
    for token in doc:
        if (token.pos_ == "NOUN" or token.pos_ == "PROPN"):
            if token.text.lower() in skill_keywords and not itemExists(token.text, list(skills)):
                skills.add(token.text)
            if token.text.lower() in cert_keywords:
                certs.add(token.text)
    print(f"Extracted skills: {skills}")
    print(f"Extracted certs: {certs}")
    if len(skills) > 0 or (len(certs) > 0 ):
        jobDetails = JobDetailsResponse(skills=[], certs=[])
        jobDetails.skills = list(skills)
        jobDetails.certs = list(certs)
        response[job.job_id] = jobDetails

def itemExists(text: str, currList: list) -> bool: #handle edge case for skills like ".Net" and ".NET"
    return text.lower() in [x.lower() for x in currList]
