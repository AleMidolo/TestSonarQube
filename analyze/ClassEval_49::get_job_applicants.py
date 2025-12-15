def get_job_applicants(self, job):
        """
        यह फ़ंक्शन उम्मीदवार की जानकारी प्राप्त करने के लिए उपयोग किया जाता है, और matches_requirements फ़ंक्शन को कॉल करके उन उम्मीदवारों की जानकारी लौटाता है जो आवश्यकताओं को पूरा करते हैं।
        :param job: पद की जानकारी, dict.
        :return: उन उम्मीदवारों की जानकारी जो आवश्यकताओं को पूरा करते हैं, list.
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        >>> jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0])
        [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]
        """
        applicants = []
        for resume in self.resumes:
            if all(skill in resume['skills'] for skill in job['requirements']):
                applicants.append(resume)
        return applicants