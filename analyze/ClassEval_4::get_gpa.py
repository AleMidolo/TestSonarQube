def get_gpa(self, name):
    """
        Get a student's average score.
        :param name: str, student name
        :return: If the name is in the student list and the student has course scores, return the average score (float),
                 otherwise return None
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0
        """
    if name in self.students and self.students[name]['courses']:
        total_score = sum(self.students[name]['courses'].values())
        count = len(self.students[name]['courses'])
        return total_score / count
    return None