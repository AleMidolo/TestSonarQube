def post_job(self, job_title, company, requirements):
    """
    该函数用于发布职位,并将职位信息添加到 job_listings 列表中。
    :param job_title: 职位的名称,str。
    :param company: 职位所在的公司,str。
    :param requirements: 职位的要求,list。
    :return: None
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.post_job("软件工程师", "ABC 公司", ['要求1', '要求2'])
    >>> jobMarketplace.job_listings
    [{'job_title': '软件工程师', 'company': 'ABC 公司', 'requirements': ['要求1', '要求2']}]

    """
    job = {
        'job_title': job_title,
        'company': company,
        'requirements': requirements
    }
    self.job_listings.append(job)