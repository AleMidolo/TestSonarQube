def get_gpa(self, name):
    """
        Get the average score of a student.
        :param name: str, student name
        :return: if the name is present in students and this student has scores in courses, return the average score (float)
                 otherwise return None
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0
        """
    if name in self.students:
        scores = self.students[name]['courses'].values()
        if scores:
            return sum(scores) / len(scores)
    return None