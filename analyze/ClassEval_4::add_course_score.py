def add_course_score(self, name, course, score):
    """
        为self.students中的学生添加特定课程的分数
        :param name: str, 学生姓名
        :param course: str, 课程名称
        :param score: int, 课程分数
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
    if name in self.students:
        self.students[name]['courses'][course] = score