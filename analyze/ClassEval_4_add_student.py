def add_student(self, name, grade, major):
    """
        Aggiungi un nuovo studente nel dizionario self.students
        :param name: str, nome dello studente
        :param grade: int, voto dello studente
        :param major: str, indirizzo dello studente
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
        """
    self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}