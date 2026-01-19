def post_job(self, job_title, company, requirements):
    """
        Esta función se utiliza para publicar posiciones y agregar la información de la posición a la lista job_listings.
        :param job_title: El título de la posición, str.
        :param company: La empresa de la posición, str.
        :param requirements: Los requisitos de la posición, list.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        >>> jobMarketplace.job_listings
        [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}]
        """
    job = {'job_title': job_title, 'company': company, 'requirements': requirements}
    self.job_listings.append(job)