def register_class(self, student_name, class_name):
    """
        registra una classe per lo studente.
        :param student_name: str
        :param class_name: str
        :return una lista di nomi di classi a cui lo studente si è registrato
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.register_class(student_name="John", class_name="CS101")
        >>> registration_system.register_class(student_name="John", class_name="CS102")
        ["CS101", "CS102"]
        """
    if student_name not in self.students_registration_classes:
        self.students_registration_classes[student_name] = []
    if class_name not in self.students_registration_classes[student_name]:
        self.students_registration_classes[student_name].append(class_name)
    return self.students_registration_classes[student_name]