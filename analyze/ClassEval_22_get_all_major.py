def get_all_major(self):
    """
    ottieni tutte le specializzazioni nel sistema
    :return una lista di specializzazioni
    >>> registration_system = ClassRegistrationSystem()
    >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
    >>> registration_system.get_all_major(student1)
    ["Computer Science"]
    """
    majors = []
    for student in self.students:
        if "major" in student and student["major"] not in majors:
            majors.append(student["major"])
    return majors