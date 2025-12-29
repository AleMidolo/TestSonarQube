def condition_judge(self):
    """
        उपयोगकर्ता की स्थिति का निर्णय BMI मानक के आधार पर करें।
        :return: यदि उपयोगकर्ता बहुत मोटा है तो 1, यदि उपयोगकर्ता बहुत पतला है तो -1, यदि उपयोगकर्ता सामान्य है तो 0, int।
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """
    bmi = self.get_BMI()
    for std_dict in self.BMI_std:
        if self.sex in std_dict:
            bmi_range = std_dict[self.sex]
            break
    else:
        bmi_range = [20, 25]
    if bmi > bmi_range[1]:
        return 1
    elif bmi < bmi_range[0]:
        return -1
    else:
        return 0