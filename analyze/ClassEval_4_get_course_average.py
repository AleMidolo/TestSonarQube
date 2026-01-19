def get_course_average(self, course):
    """
        Obtiene la calificación media de un curso específico.
        :param course: str, nombre del curso
        :return: float, puntuaciones medias de este curso si alguien tiene puntuación de este curso, o None si nadie tiene registros.
        """
    total_score = 0
    student_count = 0
    for student in self.students.values():
        if course in student['courses']:
            total_score += student['courses'][course]
            student_count += 1
    if student_count > 0:
        return total_score / student_count
    else:
        return None