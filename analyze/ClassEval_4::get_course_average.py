def get_course_average(self, course):
    """
        Obtiene la calificación media de un curso específico.
        :param course: str, nombre del curso
        :return: float, puntuaciones medias de este curso si alguien tiene puntuación de este curso, o None si nadie tiene registros.
        """
    scores = []
    for student in self.students.values():
        if course in student['courses']:
            scores.append(student['courses'][course])
    if scores:
        return sum(scores) / len(scores)
    else:
        return None