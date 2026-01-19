def get_students_by_major(self, major):
    """
        获取该专业的所有学生
        :param major: str
        :return: 学生姓名的列表
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
    return [student['name'] for student in self.students if student['major'] == major]