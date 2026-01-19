def search_jobs(self, criteria):
    """
        此函数用于搜索职位，并返回符合要求的职位信息。
        :param criteria: 职位的要求，str。
        :return: 符合要求的职位信息，list。
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "软件工程师", "company": "ABC 公司", "requirements": ['技能1', '技能2']}]
        >>> jobMarketplace.search_jobs("技能1")
        [{'job_title': '软件工程师', 'company': 'ABC 公司', 'requirements': ['技能1', '技能2']}]
        """
    matching_jobs = []
    for job in self.job_listings:
        if criteria in job['requirements']:
            matching_jobs.append(job)
    return matching_jobs