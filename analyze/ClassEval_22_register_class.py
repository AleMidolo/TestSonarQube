def register_class(self, student_name, class_name):
    """
    Registra una clase para el estudiante.
    :param student_name: str
    :param class_name: str
    :return: una lista de nombres de clases a las que el estudiante se ha registrado
    >>> registration_system = ClassRegistrationSystem()
    >>> registration_system.register_student({"name": "John", "major": "Computer Science"})
    >>> registration_system.register_class(student_name="John", class_name="CS101")
    >>> registration_system.register_class(student_name="John", class_name="CS102")
    ["CS101", "CS102"]
    """
    if student_name not in self.students_registration_classes:
        self.students_registration_classes[student_name] = []
    self.students_registration_classes[student_name].append(class_name)
    return self.students_registration_classes[student_name]