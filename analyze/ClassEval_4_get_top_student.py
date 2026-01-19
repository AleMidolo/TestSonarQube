def get_top_student(self):
    """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.add_course_score('student 2', 'Computer Network', 97)
        >>> system.get_top_student()
        'student 2'
        """
    top_student = None
    highest_gpa = -1
    for name in self.students:
        gpa = self.get_gpa(name)
        if gpa is not None and gpa > highest_gpa:
            highest_gpa = gpa
            top_student = name
    return top_student