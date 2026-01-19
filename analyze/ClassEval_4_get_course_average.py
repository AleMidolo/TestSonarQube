def get_course_average(self, course):
    """
    Obtiene la calificación media de un curso específico.
    :param course: str, nombre del curso
    :return: float, puntuaciones medias de este curso si alguien tiene puntuación de este curso, o None si nadie tiene registros.
    """
    total_score = 0
    count = 0
    
    for student in self.students:
        if course in student.grades:
            total_score += student.grades[course]
            count += 1
    
    if count == 0:
        return None
    
    return total_score / count