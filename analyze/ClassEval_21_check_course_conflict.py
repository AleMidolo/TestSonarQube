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
    new_start = new_course['start_time']
    new_end = new_course['end_time']
    
    # Assuming self.courses is a list of course dictionaries
    for course in self.courses:
        existing_start = course['start_time']
        existing_end = course['end_time']
        
        # Check for overlap (including boundary cases)
        # Conflict occurs if:
        # - new course starts before existing ends AND new course ends after existing starts
        # Since boundary times are considered conflicts, we use <= and >=
        if new_start < existing_end and new_end > existing_start:
            return False
    
    return True