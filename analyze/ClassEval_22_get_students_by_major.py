def get_students_by_major(self, major):
    """
    obtener todos los estudiantes en la carrera
    :param major: str
    :return una lista de nombres de estudiantes
    >>> registration_system = ClassRegistrationSystem()
    >>> student1 = {"name": "John", "major": "Computer Science"}
    >>> registration_system.register_student(student1)
    >>> registration_system.get_students_by_major("Computer Science")
    ["John"]
    """
    students_in_major = []
    for student in self.students:
        if student.get("major") == major:
            students_in_major.append(student.get("name"))
    return students_in_major