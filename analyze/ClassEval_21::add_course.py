def add_course(self, course):
    """
    Aggiungi il corso alla lista self.courses se il corso non è già presente.
    :param course: dict, informazioni del corso, inclusi 'start_time', 'end_time' e 'name'
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    """
    
    if course not in self.courses and self.check_course_conflict(course):
        self.courses.append(course)