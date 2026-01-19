def get_job_applicants(self, job):
    """
    Esta función se utiliza para obtener información de los candidatos y devolver la información de los candidatos que cumplen con los requisitos llamando a la función matches_requirements.
    :param job: La información del puesto, dict.
    :return: La información de los candidatos que cumplen con los requisitos, list.
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
    >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
    >>> jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0])
    [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]

    """
    applicants = []
    for resume in self.resumes:
        if self.matches_requirements(resume, job):
            applicants.append(resume)
    return applicants