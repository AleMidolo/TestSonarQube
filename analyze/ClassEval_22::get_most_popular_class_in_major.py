def get_most_popular_class_in_major(self, major):
    """
        ottiene la classe con il maggior numero di iscrizioni nel corso di studio.
        :return  una stringa della classe più popolare in questo corso di studio
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
    max_count = max(class_counts.values())
    most_popular_classes = [class_name for class_name, count in class_counts.items() if count == max_count]
    return most_popular_classes[0] if most_popular_classes else ''