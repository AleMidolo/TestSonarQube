def get_top_student(self):
    """
        Calcola il GPA di ogni studente con il metodo get_gpa e trova lo studente con il GPA più alto
        :return: str, nome dello studente il cui GPA è il più alto
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.add_course_score('student 2', 'Computer Network', 97)
        >>> system.get_top_student()
        'student 2'
        """
    top_student = None
    top_gpa = -1.0
    for name in self.students:
        gpa = self.get_gpa(name)
        if gpa is not None and gpa > top_gpa:
            top_gpa = gpa
            top_student = name
    return top_student