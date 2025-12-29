def get_top_student(self):
    """
        用 get_gpa 方法来计算每个学生的 GPA，并找到 GPA 最高的学生
        :return: str，GPA 最高的学生的姓名
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.add_course_score('student 2', 'Computer Network', 97)
        >>> system.get_top_student()
        'student 2'
        """
    top_student = None
    top_gpa = -1.0
    for name in self.students:
        gpa = self.get_gpa(name)
        if gpa is not None and gpa > top_gpa:
            top_gpa = gpa
            top_student = name
    return top_student