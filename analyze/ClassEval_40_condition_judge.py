def condition_judge(self):
    """
        根据BMI标准判断用户的身体状况。
        :return: 如果用户过胖则返回1，如果用户过瘦则返回-1，如果用户正常则返回0，返回类型为int。
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
        """
    bmi = self.get_BMI()
    if self.sex == 'male':
        if bmi < self.BMI_std[0]['male'][0]:
            return -1
        elif bmi > self.BMI_std[0]['male'][1]:
            return 1
        else:
            return 0
    elif bmi < self.BMI_std[1]['female'][0]:
        return -1
    elif bmi > self.BMI_std[1]['female'][1]:
        return 1
    else:
        return 0