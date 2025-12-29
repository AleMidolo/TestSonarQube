def get_most_popular_class_in_major(self, major):
    """
        उस मेजर में सबसे अधिक नामांकित कक्षा प्राप्त करें।
        :return  इस मेजर में सबसे लोकप्रिय कक्षा का एक स्ट्रिंग
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Computer Science"}]
        >>> registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration_system.get_most_popular_class_in_major("Computer Science")
        "Data Structures"
        """
    class_count = {}
    for student in self.students:
        if student['major'] == major:
            student_classes = self.students_registration_classes.get(student['name'], [])
            for class_name in student_classes:
                if class_name in class_count:
                    class_count[class_name] += 1
                else:
                    class_count[class_name] = 1
    if not class_count:
        return None
    return max(class_count, key=class_count.get)