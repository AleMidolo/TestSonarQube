def condition_judge(self):
    """
        Juzgar la condición del usuario basada en el estándar de IMC.
        :return: 1 si el usuario es demasiado gordo, -1 si el usuario es demasiado delgado, 0 si el usuario es normal, int.
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