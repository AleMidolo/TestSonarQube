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
    class_counts = {}
    for student in self.students:
        if student['major'] == major and student['name'] in self.students_registration_classes:
            for class_name in self.students_registration_classes[student['name']]:
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
    if not class_counts:
        return ''
    return max(class_counts, key=class_counts.get)