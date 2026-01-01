def get_BMI(self):
    """
        Calcular el IMC basado en la altura y el peso.
        :return: IMC, que es el peso dividido por el cuadrado de la altura, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "masculino")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
    return self.weight / self.height ** 2