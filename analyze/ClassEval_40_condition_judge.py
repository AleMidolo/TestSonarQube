def condition_judge(self):
    """
    उपयोगकर्ता की स्थिति का निर्णय BMI मानक के आधार पर करें।
    :return: यदि उपयोगकर्ता बहुत मोटा है तो 1, यदि उपयोगकर्ता बहुत पतला है तो -1, यदि उपयोगकर्ता सामान्य है तो 0, int।
    >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    >>> fitnessTracker.condition_judge()
    -1

    """
    bmi = self.weight / (self.height ** 2)
    
    if bmi < 18.5:
        return -1
    elif bmi >= 25:
        return 1
    else:
        return 0