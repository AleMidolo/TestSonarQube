def get_BMI(self):
    """
    Calcola il BMI basato sull'altezza e sul peso.
    :return: BMI, che è il peso diviso per il quadrato dell'altezza, float.
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.get_BMI()
    21.604938271604937

    """
    return self.weight / (self.height ** 2)