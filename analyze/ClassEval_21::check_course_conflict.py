def check_course_conflict(self, new_course):
    """
        Prima di aggiungere un nuovo corso, controlla se l'orario del nuovo corso  è in conflitto con altri corsi.
        :param new_course: dict, informazioni del corso, inclusi 'start_time', 'end_time' e 'name'
        :return: False se l'orario del nuovo corso confligge (incluso il caso in cui due corsi abbiano lo stesso orario di confine) con altri corsi, o True altrimenti.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
    new_start = datetime.strptime(new_course['start_time'], '%H:%M')
    new_end = datetime.strptime(new_course['end_time'], '%H:%M')
    for course in self.courses:
        existing_start = datetime.strptime(course['start_time'], '%H:%M')
        existing_end = datetime.strptime(course['end_time'], '%H:%M')
        if not (new_end <= existing_start or new_start >= existing_end):
            return False
    return True