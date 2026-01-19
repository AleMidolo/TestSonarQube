def condition_judge(self):
    """
        根据BMI标准判断用户的身体状况。
        :return: 如果用户过胖则返回1，如果用户过瘦则返回-1，如果用户正常则返回0，返回类型为int。
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    bmi_std = None
    for std_dict in self.BMI_std:
        if self.sex in std_dict:
            bmi_std = std_dict[self.sex]
            break
    if bmi_std is None:
        raise ValueError(f"Invalid sex: {self.sex}. Must be 'male' or 'female'.")
    lower, upper = bmi_std
    if bmi > upper:
        return 1
    elif bmi < lower:
        return -1
    else:
        return 0