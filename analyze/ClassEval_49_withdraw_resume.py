def withdraw_resume(self, resume):
    """
        此函数用于撤回简历，并从简历列表中移除简历信息。
        :param resume: 要移除的简历信息，dict。
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        >>> jobMarketplace.resumes
        []
        """
    self.resumes.remove(resume)