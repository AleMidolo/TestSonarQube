def remove_job(self, job):
    """
    Esta función se utiliza para eliminar posiciones y eliminar la información de la posición de la lista job_listings.
    :param job: La información de la posición a ser eliminada, dict.
    :return: Ninguno
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.job_listings = [{"job_title": "Ingeniero de Software", "company": "Compañía ABC", "requirements": ['requisito1', 'requisito2']}]
    >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
    >>> jobMarketplace.job_listings
    []

    """
    if job in self.job_listings:
        self.job_listings.remove(job)