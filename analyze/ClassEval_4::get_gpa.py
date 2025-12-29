def get_gpa(self, name):
    """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this student has courses grade, return average grade(float)
                    or None otherwise
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0
        """
    if name in self.students:
        courses = self.students[name]['courses']
        if courses:
            return sum(courses.values()) / len(courses)
    return None