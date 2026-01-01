def get_all_major(self):
    """
        obtener todas las carreras en el sistema
        :return una lista de especialidades
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
    majors = []
    for student in self.students:
        if student['major'] not in majors:
            majors.append(student['major'])
    return majors