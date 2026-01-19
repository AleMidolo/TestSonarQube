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
    # Count class registrations for students in the given major
    class_count = {}
    
    # Get all students in the specified major
    students_in_major = [student["name"] for student in self.students if student["major"] == major]
    
    # Count registrations for each class
    for student_name in students_in_major:
        if student_name in self.students_registration_classes:
            for class_name in self.students_registration_classes[student_name]:
                class_count[class_name] = class_count.get(class_name, 0) + 1
    
    # Find the class with the most registrations
    if not class_count:
        return None
    
    most_popular_class = max(class_count, key=class_count.get)
    return most_popular_class