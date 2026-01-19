def get_students_by_major(self, major):
    """
    get all students in the major
    :param major: str
    :return a list of student name
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