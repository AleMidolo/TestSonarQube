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
    student_names = []
    for student in self.students:
        if student['major'] == major:
            student_names.append(student['name'])
    return student_names