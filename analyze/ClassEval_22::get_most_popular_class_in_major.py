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
    students_in_major = self.get_students_by_major(major)
    for student_name in students_in_major:
        if student_name in self.students_registration_classes:
            for class_name in self.students_registration_classes[student_name]:
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
    if not class_counts:
        return ''
    most_popular_class = max(class_counts.items(), key=lambda x: x[1])
    return most_popular_class[0]