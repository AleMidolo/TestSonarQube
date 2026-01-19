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
    def time_to_minutes(time_str):
        """Convert time string 'HH:MM' to minutes since midnight"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    new_start = time_to_minutes(new_course['start_time'])
    new_end = time_to_minutes(new_course['end_time'])
    
    # Check against all existing courses
    for course in self.courses:
        existing_start = time_to_minutes(course['start_time'])
        existing_end = time_to_minutes(course['end_time'])
        
        # Check for overlap (including boundary times)
        # Conflict exists if:
        # - new course starts before existing ends AND new course ends after existing starts
        # This includes the case where boundary times are equal
        if new_start < existing_end and new_end > existing_start:
            return False
    
    return True