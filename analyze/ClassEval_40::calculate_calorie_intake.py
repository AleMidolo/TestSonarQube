def calculate_calorie_intake(self):
        """
        根据用户的状况和基础代谢率（BMR）计算卡路里摄入量。BMR是根据用户的身高、体重、年龄和性别计算的，男性的计算公式为10 * self.weight + 6.25 * self.height - 5 * self.age + 5，女性的计算公式为10 * self.weight + 6.25 * self.height - 5 * self.age - 161。卡路里摄入量是基于BMR和用户的状况计算的，如果用户过于肥胖，卡路里摄入量为BMR * 1.2；如果用户过于瘦，卡路里摄入量为BMR * 1.6；如果用户正常，卡路里摄入量为BMR * 1.4。
        :return: 卡路里摄入量，浮点数。
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0

        """
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        condition = self.condition_judge()
        if condition == 1:  # too fat
            calorie_intake = BMR * 1.2
        elif condition == -1:  # too thin
            calorie_intake = BMR * 1.6
        else:  # normal
            calorie_intake = BMR * 1.4
        
        return calorie_intake