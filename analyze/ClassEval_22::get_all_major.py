def get_all_major(self):
    """
        ottieni tutte le specializzazioni nel sistema
        :return una lista di specializzazioni
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
    majors = set()
    for student in self.students:
        majors.add(student['major'])
    return list(majors)