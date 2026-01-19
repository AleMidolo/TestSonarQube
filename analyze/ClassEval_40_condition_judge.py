def condition_judge(self):
    """
    Juzgar la condición del usuario basada en el estándar de IMC.
    :return: 1 si el usuario es demasiado gordo, -1 si el usuario es demasiado delgado, 0 si el usuario es normal, int.
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.condition_judge()
    -1

    """
    # Calculate BMI (Body Mass Index)
    bmi = self.weight / (self.height ** 2)
    
    # Standard BMI ranges:
    # Underweight: BMI < 18.5
    # Normal: 18.5 <= BMI < 24
    # Overweight: BMI >= 24
    
    if bmi < 18.5:
        return -1  # Too thin
    elif bmi >= 24:
        return 1   # Too fat
    else:
        return 0   # Normal