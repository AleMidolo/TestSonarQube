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
    class_counts = {}
    students_in_major = self.get_students_by_major(major)
    for student_name in students_in_major:
        if student_name in self.students_registration_classes:
            for class_name in self.students_registration_classes[student_name]:
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
    if not class_counts:
        return ''
    most_popular_class = max(class_counts, key=class_counts.get)
    return most_popular_class