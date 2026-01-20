def search_jobs(self, criteria):
    """
    Esta función se utiliza para buscar posiciones y devolver la información de las posiciones que cumplen con los requisitos.
    :param criteria: Los requisitos de la posición, str.
    :return: La información de la posición que cumple con los requisitos, list.
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.job_listings = [{"job_title": "Ingeniero de Software", "company": "Compañía ABC", "requirements": ['habilidad1', 'habilidad2']}]
    >>> jobMarketplace.search_jobs("habilidad1")
    [{'job_title': 'Ingeniero de Software', 'company': 'Compañía ABC', 'requirements': ['habilidad1', 'habilidad2']}]

    """
    matching_jobs = []
    for job in self.job_listings:
        if criteria in job.get('requirements', []):
            matching_jobs.append(job)
    return matching_jobs