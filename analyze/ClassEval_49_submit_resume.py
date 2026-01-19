def submit_resume(self, name, skills, experience):
    """
    此函数用于提交简历，并将简历信息添加到简历列表中。
    :param name: 简历的名称，str。
    :param skills: 简历的技能，list。
    :param experience: 简历的经验，str。
    :return: None
    >>> jobMarketplace = JobMarketplace()
    >>> jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
    >>> jobMarketplace.resumes
    [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]

    """
    resume = {
        'name': name,
        'skills': skills,
        'experience': experience
    }
    self.resumes.append(resume)