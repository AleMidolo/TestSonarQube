def condition_judge(self):
    """
        Giudica la condizione dell'utente basata sullo standard BMI.
        :return: 1 se l'utente è troppo grasso, -1 se l'utente è troppo magro, 0 se l'utente è normale, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "maschio")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    bmi_std = None
    for std_dict in self.BMI_std:
        if 'male' in std_dict and self.sex.lower() in ['male', 'maschio']:
            bmi_std = std_dict['male']
            break
        elif 'female' in std_dict and self.sex.lower() in ['female', 'femmina']:
            bmi_std = std_dict['female']
            break
    if bmi_std is None:
        for std_dict in self.BMI_std:
            if 'male' in std_dict:
                bmi_std = std_dict['male']
                break
    if bmi < bmi_std[0]:
        return -1
    elif bmi > bmi_std[1]:
        return 1
    else:
        return 0