def calculate_calorie_intake(self):
    """
    Calcular la ingesta de calorías basada en la condición del usuario y el BMR (Tasa Metabólica Basal). El BMR se calcula en función de la altura, peso, edad y sexo del usuario; para los hombres es 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, para las mujeres es 10 * self.weight + 6.25 * self.height - 5 * self.age - 161. La ingesta de calorías se calcula en función del BMR y la condición del usuario; si el usuario tiene sobrepeso, la ingesta de calorías es BMR * 1.2, si el usuario es demasiado delgado, la ingesta de calorías es BMR * 1.6, si el usuario es normal, la ingesta de calorías es BMR * 1.4.
    :return: ingesta de calorías, float.
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.calculate_calorie_intake()
    986.0

    """
    # Calculate BMR based on gender
    if self.gender == "male":
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
    else:  # female
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
    
    # Get user condition (assuming there's a method or attribute for this)
    # Based on the context, we need to determine if user is overweight, underweight, or normal
    # This likely uses BMI or another condition attribute
    condition = self.get_condition() if hasattr(self, 'get_condition') else getattr(self, 'condition', 'normal')
    
    # Calculate calorie intake based on condition
    if condition == "overweight" or condition == "sobrepeso":
        calorie_intake = bmr * 1.2
    elif condition == "underweight" or condition == "demasiado delgado":
        calorie_intake = bmr * 1.6
    else:  # normal
        calorie_intake = bmr * 1.4
    
    return calorie_intake