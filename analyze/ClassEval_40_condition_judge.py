def condition_judge(self):
    """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    if self.sex == 'male':
        lower, upper = (20, 25)
    else:
        lower, upper = (19, 24)
    if bmi > upper:
        return 1
    elif bmi < lower:
        return -1
    else:
        return 0