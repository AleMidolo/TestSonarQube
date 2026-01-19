def calculate_calorie_intake(self):
    """
        Calcular la ingesta de calorías basada en la condición del usuario y el BMR (Tasa Metabólica Basal). El BMR se calcula en función de la altura, peso, edad y sexo del usuario; para los hombres es 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, para las mujeres es 10 * self.weight + 6.25 * self.height - 5 * self.age - 161. La ingesta de calorías se calcula en función del BMR y la condición del usuario; si el usuario tiene sobrepeso, la ingesta de calorías es BMR * 1.2, si el usuario es demasiado delgado, la ingesta de calorías es BMR * 1.6, si el usuario es normal, la ingesta de calorías es BMR * 1.4.
        :return: ingesta de calorías, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0
        """
    if self.sex == 'male':
        BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
    else:
        BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
    condition = self.condition_judge()
    if condition == 1:
        calorie_intake = BMR * 1.2
    elif condition == -1:
        calorie_intake = BMR * 1.6
    else:
        calorie_intake = BMR * 1.4
    return calorie_intake