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
    applicants = []
    for resume in self.resumes:
        if self.matches_requirements(resume, job):
            applicants.append(resume)
    return applicants