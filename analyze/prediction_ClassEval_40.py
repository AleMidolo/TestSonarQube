class FitnessTracker:
    def __init__(self, height, weight, age, sex) -> None:
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = {
            "male": [20, 25],
            "female": [19, 24]
        }

    def get_BMI(self):
        return self.weight / self.height ** 2

    def get_BMI_range(self):
        return self.BMI_std[self.sex]

    def condition_judge(self):
        BMI = self.get_BMI()
        BMI_range = self.get_BMI_range()
        if BMI > BMI_range[1]:
            return 1  # too fat
        elif BMI < BMI_range[0]:
            return -1  # too thin
        else:
            return 0  # normal

    def calculate_calorie_intake(self):
        BMR = self.calculate_BMR()
        return self.calculate_calorie_based_on_condition(BMR)

    def calculate_BMR(self):
        if self.sex == "male":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def calculate_calorie_based_on_condition(self, BMR):
        condition = self.condition_judge()
        if condition == 1:
            return BMR * 1.2  # Sedentary lifestyle
        elif condition == -1:
            return BMR * 1.6  # Active lifestyle
        else:
            return BMR * 1.4  # Moderate lifestyle