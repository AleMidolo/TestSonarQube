class FitnessTracker:
    MALE_BMI_INDEX = 0
    FEMALE_BMI_INDEX = 1
    SEDENTARY_MULTIPLIER = 1.2
    ACTIVE_MULTIPLIER = 1.6
    MODERATE_MULTIPLIER = 1.4

    def __init__(self, height, weight, age, sex) -> None:
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = [
            {"male": [20, 25]},
            {"female": [19, 24]}
        ]

    def get_BMI(self):
        return self.weight / self.height ** 2

    def get_BMI_range(self):
        if self.sex == "male":
            return self.BMI_std[self.MALE_BMI_INDEX]["male"]
        return self.BMI_std[self.FEMALE_BMI_INDEX]["female"]

    def condition_judge(self):
        BMI = self.get_BMI()
        BMI_range = self.get_BMI_range()
        if BMI > BMI_range[1]:
            return 1  # too fat
        elif BMI < BMI_range[0]:
            return -1  # too thin
        return 0  # normal

    def calculate_BMR(self):
        if self.sex == "male":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def calculate_calorie_intake(self):
        BMR = self.calculate_BMR()
        condition = self.condition_judge()
        if condition == 1:
            return BMR * self.SEDENTARY_MULTIPLIER
        elif condition == -1:
            return BMR * self.ACTIVE_MULTIPLIER
        return BMR * self.MODERATE_MULTIPLIER