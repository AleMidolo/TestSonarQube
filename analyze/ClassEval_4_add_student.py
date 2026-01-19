def add_student(self, name, grade, major):
    """
    将新学生添加到 self.students 字典中
    :param name: str, 学生姓名
    :param grade: int, 学生年级
    :param major: str, 学生专业
    >>> system.add_student('student 1', 3, 'SE')
    >>> system.students
    {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
    """
    self.students[name] = {
        'name': name,
        'grade': grade,
        'major': major,
        'courses': {}
    }