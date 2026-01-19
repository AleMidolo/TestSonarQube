def condition_judge(self):
    """
    Giudica la condizione dell'utente basata sullo standard BMI.
    :return: 1 se l'utente è troppo grasso, -1 se l'utente è troppo magro, 0 se l'utente è normale, int.
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "maschio")
    >>> fitnessTracker.condition_judge()
    -1

    """
    bmi = self.weight / (self.height ** 2)
    
    if bmi < 18.5:
        return -1
    elif bmi > 25:
        return 1
    else:
        return 0