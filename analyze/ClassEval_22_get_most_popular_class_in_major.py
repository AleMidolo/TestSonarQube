def get_most_popular_class_in_major(self, major):
    """
    获取该专业中注册人数最多的课程。
    :return  一个字符串,表示该专业中最受欢迎课程
    >>> registration_system = ClassRegistrationSystem()
    >>> registration_system.students = [{"name": "John", "major": "计算机科学"},
                                         {"name": "Bob", "major": "计算机科学"},
                                         {"name": "Alice", "major": "计算机科学"}]
    >>> registration_system.students_registration_classes = {"John": ["算法", "数据结构"],
                                        "Bob": ["操作系统", "数据结构", "算法"]}
    >>> registration_system.get_most_popular_class_in_major("计算机科学")
    "数据结构"
    """
    from collections import Counter
    
    # Get all students in the specified major
    students_in_major = [student["name"] for student in self.students if student["major"] == major]
    
    # Count all classes registered by students in this major
    class_counts = Counter()
    for student_name in students_in_major:
        if student_name in self.students_registration_classes:
            classes = self.students_registration_classes[student_name]
            class_counts.update(classes)
    
    # Return the most common class
    if class_counts:
        return class_counts.most_common(1)[0][0]
    return None