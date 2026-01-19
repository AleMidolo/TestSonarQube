def add_student(self, name, grade, major):
    """
    Agrega un nuevo estudiante al diccionario self.students
    :param name: str, nombre del estudiante
    :param grade: int, grado del estudiante
    :param major: str, carrera universitaria del estudiante
    >>> system.add_student('student 1', 3, 'SE')
    >>> system.students
    {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
    """
    self.students[name] = {
        'name': name,
        'grade': grade,
        'major': major,
        'courses': {}
    }