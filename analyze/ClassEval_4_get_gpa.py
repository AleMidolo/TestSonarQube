def get_gpa(self, name):
    """
    Obtener la nota promedio de un estudiante.
    :param name: str, nombre del estudiante
    :return: si el nombre está en los estudiantes y este estudiante tiene calificaciones de cursos, 
             devuelve la nota promedio (float) o None en caso contrario
    >>> system.add_student('student 1', 3, 'SE')
    >>> system.add_course_score('student 1', 'math', 94)
    >>> system.add_course_score('student 1', 'Computer Network', 92)
    >>> system.get_gpa('student 1')
    93.0

    """
    # Check if the student exists
    if name not in self.students:
        return None
    
    # Get the student's course scores
    student = self.students[name]
    
    # Check if the student has a courses attribute and it's not empty
    if not hasattr(student, 'courses') or not student.courses:
        return None
    
    # Calculate the average of all course scores
    total_score = sum(student.courses.values())
    num_courses = len(student.courses)
    
    return float(total_score / num_courses)