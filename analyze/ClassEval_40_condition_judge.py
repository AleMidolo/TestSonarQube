def condition_judge(self):
    """
    根据BMI标准判断用户的身体状况。
    :return: 如果用户过胖则返回1，如果用户过瘦则返回-1，如果用户正常则返回0，返回类型为int。
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.condition_judge()
    -1

    """
    # Calculate BMI: weight (kg) / height (m)^2
    bmi = self.weight / (self.height ** 2)
    
    # BMI standards:
    # Underweight: BMI < 18.5
    # Normal: 18.5 <= BMI < 24
    # Overweight/Obese: BMI >= 24
    
    if bmi < 18.5:
        return -1  # 过瘦
    elif bmi >= 24:
        return 1   # 过胖
    else:
        return 0   # 正常