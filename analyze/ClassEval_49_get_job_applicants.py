def get_job_applicants(self, job):
    """
        This function is used to obtain candidate information,and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job: The position information,dict.
        :return: The candidate information that meets the requirements,list.
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
    matching_applicants = []
    for resume in self.resumes:
        if matches_requirements(resume, job['requirements']):
            matching_applicants.append(resume)
    return matching_applicants