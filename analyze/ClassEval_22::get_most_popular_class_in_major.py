def get_most_popular_class_in_major(self, major):
    """
        获取该专业中注册人数最多的课程。
        :return  一个字符串，表示该专业中最受欢迎课程
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "计算机科学"},
                                             {"name": "Bob", "major": "计算机科学"},
                                             {"name": "Alice", "major": "计算机科学"}]
        >>> registration_system.students_registration_classes = {"John": ["算法", "数据结构"],
                                            "Bob": ["操作系统", "数据结构", "算法"]}
        >>> registration_system.get_most_popular_class_in_major("计算机科学")
        "数据结构"
        """
    class_counts = {}
    for student in self.students:
        if student['major'] == major:
            student_name = student['name']
            if student_name in self.students_registration_classes:
                for class_name in self.students_registration_classes[student_name]:
                    if class_name in class_counts:
                        class_counts[class_name] += 1
                    else:
                        class_counts[class_name] = 1
    if not class_counts:
        return ''
    max_count = max(class_counts.values())
    most_popular_classes = [class_name for class_name, count in class_counts.items() if count == max_count]
    return most_popular_classes[0] if most_popular_classes else ''