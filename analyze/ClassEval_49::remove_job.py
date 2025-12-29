def remove_job(self, job):
    """
        此函数用于移除职位，并从 job_listings 列表中移除职位信息。
        :param job: 要移除的职位信息，dict。
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "软件工程师", "company": "ABC 公司", "requirements": ['要求1', '要求2']}]
        >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        >>> jobMarketplace.job_listings
        []
        """
    self.job_listings.remove(job)