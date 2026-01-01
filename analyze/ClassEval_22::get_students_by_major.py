def get_students_by_major(self, major):
    """
        ottieni tutti gli studenti nel corso di laurea
        :param major: str
        :return una lista di nomi degli studenti
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
    return [student['name'] for student in self.students if student['major'] == major]