def get_most_popular_class_in_major(self, major):
    """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Computer Science"}]
        >>> registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration_system.get_most_popular_class_in_major("Computer Science")
        "Data Structures"
        """
    class_enrollment = {}
    for student in self.students:
        if student['major'] == major:
            student_classes = self.students_registration_classes.get(student['name'], [])
            for class_name in student_classes:
                if class_name in class_enrollment:
                    class_enrollment[class_name] += 1
                else:
                    class_enrollment[class_name] = 1
    if not class_enrollment:
        return ''
    most_popular_class = max(class_enrollment, key=class_enrollment.get)
    return most_popular_class