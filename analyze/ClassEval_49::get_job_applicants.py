def get_job_applicants(self, job):
    """
        Questa funzione viene utilizzata per ottenere informazioni sui candidati e restituire le informazioni sui candidati che soddisfano i requisiti chiamando la funzione matches_requirements.
        :param job: Le informazioni sulla posizione, dict.
        :return: Le informazioni sui candidati che soddisfano i requisiti, list.
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "esperienza"}]
        >>> jobMarketplace.job_listings = [{"job_title": "Ingegnere del Software", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        >>> jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0])
        [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'esperienza'}]

        """

    def matches_requirements(resume, job_requirements):
        """Helper function to check if resume matches job requirements."""
        resume_skills = set((skill.lower() for skill in resume['skills']))
        job_reqs = set((req.lower() for req in job_requirements))
        return job_reqs.issubset(resume_skills)
    matching_applicants = []
    job_requirements = job.get('requirements', [])
    for resume in self.resumes:
        if matches_requirements(resume, job_requirements):
            matching_applicants.append(resume)
    return matching_applicants