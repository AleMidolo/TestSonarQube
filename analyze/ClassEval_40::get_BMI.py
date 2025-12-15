def get_BMI(self):
        """
        根据身高和体重计算BMI。
        :return: BMI，即体重除以身高的平方，浮点数。
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
        return self.weight / (self.height ** 2)