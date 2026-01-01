def search_jobs(self, criteria):
    """
        This function is used to search for positions,and return the position information that meets the requirements.
        :param criteria: The requirements of the position,str.
        :return: The position information that meets the requirements,list.
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        >>> jobMarketplace.search_jobs("skill1")
        [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']}]

        """
    matching_jobs = []
    for job in self.job_listings:
        if criteria.lower() in job['job_title'].lower() or criteria.lower() in job['company'].lower() or any((criteria.lower() in str(req).lower() for req in job['requirements'])):
            matching_jobs.append(job)
    return matching_jobs