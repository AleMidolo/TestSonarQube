def post_job(self, job_title, company, requirements):
    """
        Questa funzione viene utilizzata per pubblicare posizioni e aggiungere le informazioni sulla posizione alla lista job_listings.
        :param job_title: Il titolo della posizione, str.
        :param company: L'azienda della posizione, str.
        :param requirements: I requisiti della posizione, list.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        >>> jobMarketplace.job_listings
        [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}]
        """
    job = {'job_title': job_title, 'company': company, 'requirements': requirements}
    self.job_listings.append(job)