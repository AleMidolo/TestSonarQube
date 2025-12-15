def withdraw_resume(self, resume):
        """
        Questa funzione viene utilizzata per ritirare i curriculum e rimuovere le informazioni del curriculum dall'elenco dei curriculum.
        :param resume: Le informazioni del curriculum da rimuovere, dict.
        :return: Nessuno
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        >>> jobMarketplace.resumes
        []
        """
        self.resumes.remove(resume)