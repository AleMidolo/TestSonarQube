def get_all_students_with_fail_course(self):
    """
    Obtener todos los estudiantes que tienen alguna calificación por debajo de 60
    :return: lista de str, nombre del estudiante
    >>> system.add_course_score('student 1', 'Society', 59)
    >>> system.get_all_students_with_fail_course()
    ['student 1']
    """
    students_with_fail = []
    
    for student_name, courses in self.students.items():
        for course_name, score in courses.items():
            if score < 60:
                students_with_fail.append(student_name)
                break  # No need to check other courses for this student
    
    return students_with_fail