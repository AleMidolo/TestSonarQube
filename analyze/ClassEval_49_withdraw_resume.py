def withdraw_resume(self, resume):
    """
        Esta función se utiliza para retirar currículos y eliminar la información del currículo de la lista de currículos.
        :param resume: La información del currículo a ser eliminada, dict.
        :return: Ninguno
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        >>> jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        >>> jobMarketplace.resumes
        []
        """
    self.resumes.remove(resume)