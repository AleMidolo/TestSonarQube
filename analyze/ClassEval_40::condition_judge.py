def condition_judge(self):
    """
        Juzgar la condición del usuario basada en el estándar de IMC.
        :return: 1 si el usuario es demasiado gordo, -1 si el usuario es demasiado delgado, 0 si el usuario es normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    bmi_std = None
    for std in self.BMI_std:
        if self.sex in std:
            bmi_std = std[self.sex]
            break
    if bmi_std is None:
        return 0
    if bmi > bmi_std[1]:
        return 1
    elif bmi < bmi_std[0]:
        return -1
    else:
        return 0