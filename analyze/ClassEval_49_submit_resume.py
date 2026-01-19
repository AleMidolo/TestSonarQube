def submit_resume(self, name, skills, experience):
    """
    यह फ़ंक्शन रिज़्यूमे जमा करने के लिए उपयोग किया जाता है, और रिज़्यूमे की जानकारी को रिज़्यूमे सूची में जोड़ता है।
    :param name: रिज़्यूमे का नाम, str.
    :param skills: रिज़्यूमे की क्षमताएँ, list.
    :param experience: रिज़्यूमे का अनुभव, str.
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