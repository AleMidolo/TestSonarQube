def calculate_calorie_intake(self):
    """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate), BMR is calculated based on the user's height, weight, age, and sex, male is 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, female is 10 * self.weight + 6.25 * self.height - 5 * self.age - 161, and the calorie intake is calculated based on the BMR and the user's condition, if the user is too fat, the calorie intake is BMR * 1.2, if the user is too thin, the calorie intake is BMR * 1.6, if the user is normal, the calorie intake is BMR * 1.4.
        :return: calorie intake, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0
        """
    if self.sex == 'male':
        BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
    else:
        BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
    condition = self.condition_judge()
    if condition == 1:
        calorie_intake = BMR * 1.2
    elif condition == -1:
        calorie_intake = BMR * 1.6
    else:
        calorie_intake = BMR * 1.4
    return calorie_intake