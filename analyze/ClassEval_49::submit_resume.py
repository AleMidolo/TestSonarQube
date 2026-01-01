def submit_resume(self, name, skills, experience):
    """
        Esta función se utiliza para enviar currículos y agregar la información del currículo a la lista de currículos.
        :param name: El nombre del currículo, str.
        :param skills: Las habilidades del currículo, list.
        :param experience: La experiencia del currículo, str.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        >>> jobMarketplace.resumes
        [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]
        """
    resume = {'name': name, 'skills': skills, 'experience': experience}
    self.resumes.append(resume)