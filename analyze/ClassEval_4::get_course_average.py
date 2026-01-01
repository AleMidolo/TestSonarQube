def get_course_average(self, course):
    """
        Ottieni il punteggio medio di un corso specifico.
        :param course: str, nome del corso
        :return: float, punteggi medi di questo corso se qualcuno ha un punteggio di questo corso, o None se nessuno ha registrazioni.
        """
    scores = []
    for student in self.students.values():
        if course in student['courses']:
            scores.append(student['courses'][course])
    if scores:
        return sum(scores) / len(scores)
    else:
        return None