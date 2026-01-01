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
    class_count = {}
    for student in self.get_students_by_major(major):
        classes = self.students_registration_classes.get(student, [])
        for cls in classes:
            if cls in class_count:
                class_count[cls] += 1
            else:
                class_count[cls] = 1
    if not class_count:
        return ''
    return max(class_count, key=class_count.get)