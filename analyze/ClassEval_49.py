class JobMarketplace:
    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        job = self.create_job(job_title, company, requirements)
        self.job_listings.append(job)

    def create_job(self, job_title, company, requirements):
        return {"job_title": job_title, "company": company, "requirements": requirements}

    def remove_job(self, job):
        self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        resume = self.create_resume(name, skills, experience)
        self.resumes.append(resume)

    def create_resume(self, name, skills, experience):
        return {"name": name, "skills": skills, "experience": experience}

    def withdraw_resume(self, resume):
        self.resumes.remove(resume)

    def search_jobs(self, criteria):
        return [job_listing for job_listing in self.job_listings if self.matches_criteria(job_listing, criteria)]

    def matches_criteria(self, job_listing, criteria):
        return (criteria.lower() in job_listing["job_title"].lower() or 
                criteria.lower() in [r.lower() for r in job_listing["requirements"]])

    def get_job_applicants(self, job):
        return [resume for resume in self.resumes if self.matches_requirements(resume, job["requirements"])]

    @staticmethod
    def matches_requirements(resume, requirements):
        return all(skill in requirements for skill in resume["skills"])