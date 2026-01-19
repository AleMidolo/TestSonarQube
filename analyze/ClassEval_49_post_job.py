def post_job(self, job_title, company, requirements):
    """
        यह फ़ंक्शन पदों को प्रकाशित करने के लिए उपयोग किया जाता है, और पद की जानकारी को job_listings सूची में जोड़ता है।
        :param job_title: पद का शीर्षक, str.
        :param company: पद का कंपनी, str.
        :param requirements: पद की आवश्यकताएँ, list.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        >>> jobMarketplace.job_listings
        [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}]
        """
    job = {'job_title': job_title, 'company': company, 'requirements': requirements}
    self.job_listings.append(job)