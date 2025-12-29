def condition_judge(self):
    """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
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
        raise ValueError(f'Invalid sex: {self.sex}')
    if bmi < bmi_std[0]:
        return -1
    elif bmi > bmi_std[1]:
        return 1
    else:
        return 0