def get_all_students_with_fail_course(self):
    """
        Get all students who have a score lower than 60
        :return: list of str, names of students
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
    failed_students = []
    for student in self.students.values():
        for score in student['courses'].values():
            if score < 60:
                failed_students.append(student['name'])
                break
    return failed_students