class FitnessTracker: 
    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = [
            {"male": [20, 25]},
            {"female": [19, 24]}
        ]

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divide by the square of height, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
        return self.weight / self.height ** 2
    
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
        """
        BMI = self.get_BMI()
        if self.sex == "male":
            BMI_range = self.BMI_std[0]["male"]
        else:
            BMI_range = self.BMI_std[1]["female"]
        if BMI > BMI_range[1]:
            # too fat
            return 1
        elif BMI < BMI_range[0]:
            # too thin
            return -1
        else:
            # normal
            return 0
    
    def calculate_calorie_intake(self):
        """
        Calcola l'apporto calorico basato sulla condizione dell'utente e sul BMR (Tasso Metabolico Basale). 
        Il BMR è calcolato in base all'altezza, al peso, all'età e al sesso dell'utente; 
        per i maschi è 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, 
        per le femmine è 10 * self.weight + 6.25 * self.height - 5 * self.age - 161. 
        L'apporto calorico è calcolato in base al BMR e alla condizione dell'utente; 
        se l'utente è troppo grasso, l'apporto calorico è BMR * 1.2, 
        se l'utente è troppo magro, l'apporto calorico è BMR * 1.6, 
        se l'utente è normale, l'apporto calorico è BMR * 1.4.
        :return: apporto calorico, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0
        """
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        
        condition = self.condition_judge()
        if condition == 1:  # too fat
            return BMR * 1.2
        elif condition == -1:  # too thin
            return BMR * 1.6
        else:  # normal
            return BMR * 1.4