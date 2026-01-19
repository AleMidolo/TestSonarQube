def get_course_average(self, course):
    """
    Ottieni il punteggio medio di un corso specifico.
    :param course: str, nome del corso
    :return: float, punteggi medi di questo corso se qualcuno ha un punteggio di questo corso, o None se nessuno ha registrazioni.
    """
    total_score = 0
    count = 0
    
    for student in self.students:
        if course in student.grades:
            total_score += student.grades[course]
            count += 1
    
    if count == 0:
        return None
    
    return total_score / count