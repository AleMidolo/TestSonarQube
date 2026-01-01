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
    if self.sex == 'male':
        BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
    else:
        BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
    condition = self.condition_judge()
    if condition == 1:
        calorie_intake = BMR * 1.2
    elif condition == -1:
        calorie_intake = BMR * 1.6
    else:
        calorie_intake = BMR * 1.4
    return calorie_intake