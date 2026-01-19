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
    
    # Judge condition based on BMI standards
    # BMI < 18.5: underweight (too thin)
    # 18.5 <= BMI < 25: normal weight
    # BMI >= 25: overweight (too fat)
    
    if bmi < 18.5:
        return -1  # too thin
    elif bmi >= 25:
        return 1   # too fat
    else:
        return 0   # normal