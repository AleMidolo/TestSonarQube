def add_course_score(self, name, course, score):
    """
    Aggiungi il punteggio di un corso specifico per lo studente in self.students
    :param name: str, nome dello studente
    :param course: str, nome del corso
    :param score: int, punteggio del corso
    >>> system.add_student('studente 1', 3, 'SE')
    >>> system.add_course_score('studente 1', 'matematica', 94)
    >>> system.students
    {'studente 1': {'name': 'studente 1', 'grade': 3, 'major': 'SE', 'courses': {'matematica': 94}}}
    """
    if name in self.students:
        if 'courses' not in self.students[name]:
            self.students[name]['courses'] = {}
        self.students[name]['courses'][course] = score