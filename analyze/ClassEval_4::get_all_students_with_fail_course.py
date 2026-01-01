def get_all_students_with_fail_course(self):
    """
        उन सभी छात्रों को प्राप्त करें जिनका कोई भी स्कोर 60 से कम है
        :return: str की सूची, छात्र का नाम
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
    failing_students = []
    for name, student in self.students.items():
        for score in student['courses'].values():
            if score < 60:
                failing_students.append(name)
                break
    return failing_students