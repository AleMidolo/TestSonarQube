def condition_judge(self):
    """
        उपयोगकर्ता की स्थिति का निर्णय BMI मानक के आधार पर करें।
        :return: यदि उपयोगकर्ता बहुत मोटा है तो 1, यदि उपयोगकर्ता बहुत पतला है तो -1, यदि उपयोगकर्ता सामान्य है तो 0, int।
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    bmi_range = None
    for std in self.BMI_std:
        if self.sex in std:
            bmi_range = std[self.sex]
            break
    if bmi_range is None:
        raise ValueError(f"Invalid sex: {self.sex}. Must be 'male' or 'female'.")
    lower, upper = bmi_range
    if bmi < lower:
        return -1
    elif bmi > upper:
        return 1
    else:
        return 0