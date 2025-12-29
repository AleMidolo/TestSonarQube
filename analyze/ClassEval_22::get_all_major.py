def get_all_major(self):
    """
        获取系统中的所有专业
        :return 返回专业列表
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "计算机科学"}],
        >>> registration_system.get_all_major(student1)
        ["计算机科学"]
        """
    major_set = set()
    for student in self.students:
        major_set.add(student['major'])
    return list(major_set)