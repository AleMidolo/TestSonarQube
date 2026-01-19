def is_free_at(self, check_time):
    """
        cambia el formato de tiempo a '%H:%M' y verifica si hay disponibilidad en el aula.
        :param check_time: str, el tiempo que necesita ser verificado
        :return: True si el check_time no entra en conflicto con el horario de ningún curso, o False en caso contrario.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
    check_time_dt = datetime.strptime(check_time, '%H:%M')
    for course in self.courses:
        start_time = datetime.strptime(course['start_time'], '%H:%M')
        end_time = datetime.strptime(course['end_time'], '%H:%M')
        if start_time <= check_time_dt <= end_time:
            return False
    return True