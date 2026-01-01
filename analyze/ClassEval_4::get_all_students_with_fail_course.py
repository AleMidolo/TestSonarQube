def get_all_students_with_fail_course(self):
    """
        Get all students who have any score blow 60
        :return: list of str ,student name
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