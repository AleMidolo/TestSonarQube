def remove_job(self, job):
    """
        यह फ़ंक्शन पदों को हटाने के लिए उपयोग किया जाता है, और job_listings सूची से पद की जानकारी को हटाता है।
        :param job: हटाने के लिए पद की जानकारी, dict.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "सॉफ़्टवेयर इंजीनियर", "company": "एबीसी कंपनी", "requirements": ['आवश्यकता1', 'आवश्यकता2']}]
        >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        >>> jobMarketplace.job_listings
        []

        """
    self.job_listings.remove(job)