def get_all_students_with_fail_course(self):
    """
        उन सभी छात्रों को प्राप्त करें जिनका कोई भी स्कोर 60 से कम है
        :return: str की सूची, छात्र का नाम
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
    failed_students = []
    for name, student in self.students.items():
        if any((score < 60 for score in student['courses'].values())):
            failed_students.append(name)
    return failed_students