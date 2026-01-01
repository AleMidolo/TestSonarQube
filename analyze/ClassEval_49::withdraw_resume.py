def withdraw_resume(self, resume):
    """
        यह फ़ंक्शन रिज़्यूमे को वापस लेने के लिए उपयोग किया जाता है, और रिज़्यूमे सूची से रिज़्यूमे की जानकारी को हटा देता है।
        :param resume: हटाई जाने वाली रिज़्यूमे की जानकारी, dict.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        >>> jobMarketplace.resumes
        []
        """
    self.resumes.remove(resume)