def register_class(self, student_name, class_name):
    """
        छात्र के लिए एक कक्षा पंजीकृत करें।
        :param student_name: str
        :param class_name: str
        :return छात्र द्वारा पंजीकृत कक्षाओं के नामों की सूची
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