def remove_course(self, course):
    """
    Rimuovi il corso dalla lista self.courses se il corso era presente.
    :param course: dict, informazioni del corso, inclusi 'start_time', 'end_time' e 'name'
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.remove_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.courses
    []
    """
    
    if course in self.courses:
        self.courses.remove(course)