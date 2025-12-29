def calculate_calorie_intake(self):
    """
        उपयोगकर्ता की स्थिति और BMR (बेसल मेटाबॉलिक रेट) के आधार पर कैलोरी सेवन की गणना करें। BMR उपयोगकर्ता की ऊँचाई, वजन, उम्र और लिंग के आधार पर गणना की जाती है, पुरुष के लिए BMR है 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, महिला के लिए BMR है 10 * self.weight + 6.25 * self.height - 5 * self.age - 161, और कैलोरी सेवन BMR और उपयोगकर्ता की स्थिति के आधार पर गणना की जाती है, यदि उपयोगकर्ता बहुत मोटा है, तो कैलोरी सेवन BMR * 1.2 है, यदि उपयोगकर्ता बहुत पतला है, तो कैलोरी सेवन BMR * 1.6 है, यदि उपयोगकर्ता सामान्य है, तो कैलोरी सेवन BMR * 1.4 है।
        :return: कैलोरी सेवन, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0

        """
    if self.sex == 'male':
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
    else:
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
    condition = self.condition_judge()
    if condition == 1:
        calorie_intake = bmr * 1.2
    elif condition == -1:
        calorie_intake = bmr * 1.6
    else:
        calorie_intake = bmr * 1.4
    return calorie_intake