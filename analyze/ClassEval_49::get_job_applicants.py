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
        applicants = []
        for resume in self.resumes:
            if all(skill in resume["skills"] for skill in job["requirements"]):
                applicants.append(resume)
        return applicants