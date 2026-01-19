def get_top_student(self):
    """
        Calcula el GPA de cada estudiante con el método get_gpa y encuentra al estudiante con el GPA más alto
        :return: str, nombre del estudiante cuyo GPA es el más alto
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