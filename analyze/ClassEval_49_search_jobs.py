def search_jobs(self, criteria):
    """
    यह फ़ंक्शन पदों की खोज करने के लिए उपयोग किया जाता है, और उन पदों की जानकारी लौटाता है जो आवश्यकताओं को पूरा करते हैं।
    :param criteria: पद की आवश्यकताएँ, str.
    :return: उन पदों की जानकारी जो आवश्यकताओं को पूरा करते हैं, list.
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.job_listings = [{"job_title": "सॉफ़्टवेयर इंजीनियर", "company": "एबीसी कंपनी", "requirements": ['skill1', 'skill2']}]
    >>> jobMarketplace.search_jobs("skill1")
    [{'job_title': 'सॉफ़्टवेयर इंजीनियर', 'company': 'एबीसी कंपनी', 'requirements': ['skill1', 'skill2']}]

    """
    matching_jobs = []
    for job in self.job_listings:
        if criteria in job.get('requirements', []):
            matching_jobs.append(job)
    return matching_jobs