def condition_judge(self):
    """
        Giudica la condizione dell'utente basata sullo standard BMI.
        :return: 1 se l'utente è troppo grasso, -1 se l'utente è troppo magro, 0 se l'utente è normale, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "maschio")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    if self.sex == 'male':
        bmi_min, bmi_max = (20, 25)
    else:
        bmi_min, bmi_max = (19, 24)
    if bmi > bmi_max:
        return 1
    elif bmi < bmi_min:
        return -1
    else:
        return 0