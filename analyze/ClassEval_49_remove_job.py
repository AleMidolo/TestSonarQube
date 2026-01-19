def remove_job(self, job):
    """
    Questa funzione viene utilizzata per rimuovere posizioni e rimuovere le informazioni sulla posizione dalla lista job_listings.
    :param job: Le informazioni sulla posizione da rimuovere, dict.
    :return: None
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}]
    >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
    >>> jobMarketplace.job_listings
    []
    """
    if job in self.job_listings:
        self.job_listings.remove(job)