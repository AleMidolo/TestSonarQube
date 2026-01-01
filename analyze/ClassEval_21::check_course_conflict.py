def check_course_conflict(self, new_course):
    """
        Antes de agregar un nuevo curso, verifica si el horario del nuevo curso entra en conflicto con algún otro curso.
        :param new_course: dict, información del curso, incluyendo 'start_time', 'end_time' y 'name'
        :return: False si el horario del nuevo curso entra en conflicto (incluyendo si dos cursos tienen el mismo tiempo límite) con otros cursos, o True en caso contrario.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
    new_start = datetime.strptime(new_course['start_time'], '%H:%M')
    new_end = datetime.strptime(new_course['end_time'], '%H:%M')
    for course in self.courses:
        start = datetime.strptime(course['start_time'], '%H:%M')
        end = datetime.strptime(course['end_time'], '%H:%M')
        if not (new_end <= start or new_start >= end):
            return False
    return True