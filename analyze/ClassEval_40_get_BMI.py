def get_BMI(self):
    """
    ऊँचाई और वजन के आधार पर BMI की गणना करें।
    :return: BMI, जो वजन को ऊँचाई के वर्ग से विभाजित करता है, float।
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.get_BMI()
    21.604938271604937

    """
    return self.weight / (self.height ** 2)