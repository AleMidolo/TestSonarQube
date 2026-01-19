def get_all_students_with_fail_course(self):
    """
        Obtener todos los estudiantes que tienen alguna calificación por debajo de 60
        :return: lista de str, nombre del estudiante
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
    failed_students = []
    for name, student in self.students.items():
        for score in student['courses'].values():
            if score < 60:
                failed_students.append(name)
                break
    return failed_students