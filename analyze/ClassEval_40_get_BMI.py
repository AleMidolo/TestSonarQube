def get_BMI(self):
    """
        Calculate the BMI based on the height and weight.
        :return: BMI,which is the weight divide by the square of height, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
    return self.weight / self.height ** 2