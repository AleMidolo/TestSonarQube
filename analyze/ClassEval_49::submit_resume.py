def submit_resume(self, name, skills, experience):
        """
        Questa funzione viene utilizzata per inviare i curriculum e aggiungere le informazioni del curriculum alla lista dei curriculum.
        :param name: Il nome del curriculum, str.
        :param skills: Le competenze del curriculum, list.
        :param experience: L'esperienza del curriculum, str.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        >>> jobMarketplace.resumes
        [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]

        """
        resume = {"name": name, "skills": skills, "experience": experience}
        self.resumes.append(resume)