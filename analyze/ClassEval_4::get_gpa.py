def get_gpa(self, name):
    """
        获取一个学生的平均成绩。
        :param name: 字符串, 学生姓名
        :return: 如果姓名在学生列表中并且该学生有课程成绩，返回平均成绩（浮点数），
                    否则返回 None
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0
        """
    if name in self.students and self.students[name]['courses']:
        total_score = sum(self.students[name]['courses'].values())
        count_courses = len(self.students[name]['courses'])
        return total_score / count_courses
    return None