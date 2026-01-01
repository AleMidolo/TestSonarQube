def add_course_score(self, name, course, score):
    """
        Agregar la calificación de un curso específico para el estudiante en self.students
        :param name: str, nombre del estudiante
        :param course: str, nombre del curso
        :param score: int, puntuación del curso
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
    if name in self.students:
        self.students[name]['courses'][course] = score