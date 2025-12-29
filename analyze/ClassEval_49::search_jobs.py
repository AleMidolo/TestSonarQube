def search_jobs(self, criteria):
    """
        Questa funzione viene utilizzata per cercare posizioni e restituire le informazioni sulla posizione che soddisfano i requisiti.
        :param criteria: I requisiti della posizione, str.
        :return: Le informazioni sulla posizione che soddisfano i requisiti, list.
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        >>> jobMarketplace.search_jobs("skill1")
        [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']}]

        """
    matching_jobs = []
    for job in self.job_listings:
        if criteria in job['requirements']:
            matching_jobs.append(job)
    return matching_jobs