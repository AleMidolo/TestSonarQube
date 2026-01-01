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
    if name in self.students:
        scores = self.students[name]['courses'].values()
        if scores:
            return sum(scores) / len(scores)
    return None