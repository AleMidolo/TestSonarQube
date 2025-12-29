def condition_judge(self):
    """
        Giudica la condizione dell'utente basata sullo standard BMI.
        :return: 1 se l'utente è troppo grasso, -1 se l'utente è troppo magro, 0 se l'utente è normale, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
        """
    bmi = self.get_BMI()
    if self.sex == 'male':
        if bmi < 20:
            return -1
        elif bmi > 25:
            return 1
        else:
            return 0
    elif bmi < 19:
        return -1
    elif bmi > 24:
        return 1
    else:
        return 0