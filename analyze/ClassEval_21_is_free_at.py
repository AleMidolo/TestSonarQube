def is_free_at(self, check_time):
    """
        cambia il formato dell'orario in '%H:%M' e verifica se l'orario è libero o meno nell'aula.
        :param check_time: str, l'orario da controllare
        :return: True se l'orario di controllo non confligge con gli orari di nessun corso, altrimenti False.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'matematica', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
    check_dt = datetime.strptime(check_time, '%H:%M')
    for course in self.courses:
        start_time = datetime.strptime(course['start_time'], '%H:%M')
        end_time = datetime.strptime(course['end_time'], '%H:%M')
        if start_time <= check_dt <= end_time:
            return False
    return True