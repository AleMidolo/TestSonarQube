def get_course_average(self, course):
    """
        Ottieni il punteggio medio di un corso specifico.
        :param course: str, nome del corso
        :return: float, punteggi medi di questo corso se qualcuno ha un punteggio di questo corso, o None se nessuno ha registrazioni.
        """
    total_score = 0
    count = 0
    for student in self.students.values():
        if course in student['courses']:
            total_score += student['courses'][course]
            count += 1
    return total_score / count if count > 0 else None