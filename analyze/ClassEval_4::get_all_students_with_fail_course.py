def get_all_students_with_fail_course(self):
    """
        获取所有有任何分数低于60的学生
        :return: 字符串的列表，学生姓名
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
    failed_students = []
    for name, student in self.students.items():
        for score in student['courses'].values():
            if score < 60:
                failed_students.append(name)
                break
    return failed_students