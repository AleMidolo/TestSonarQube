def add_student(self, name, grade, major):
    """
    self.students dict में एक नया छात्र जोड़ें
    :param name: str, छात्र का नाम
    :param grade: int, छात्र का ग्रेड
    :param major: str, छात्र का मेजर
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