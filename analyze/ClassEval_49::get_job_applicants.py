def get_job_applicants(self, job):
    """
        此函数用于获取候选人信息，并通过调用 matches_requirements 函数返回符合要求的候选人信息。
        :param job: 职位信息，dict。
        :return: 符合要求的候选人信息，list。
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        >>> jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0])
        [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]
        """

    def matches_requirements(resume, job_requirements):
        """Helper function to check if resume matches job requirements."""
        resume_skills = set((skill.lower() for skill in resume['skills']))
        job_reqs = set((req.lower() for req in job_requirements))
        return job_reqs.issubset(resume_skills)
    qualified_applicants = []
    job_requirements = job.get('requirements', [])
    for resume in self.resumes:
        if matches_requirements(resume, job_requirements):
            qualified_applicants.append(resume)
    return qualified_applicants