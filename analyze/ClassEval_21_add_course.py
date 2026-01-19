def add_course(self, course):
    """
    Agrega el curso a la lista self.courses si el curso no estaba en ella.
    :param course: dict, información del curso, incluyendo 'start_time', 'end_time' y 'name'
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    """
    if course not in self.courses:
        self.courses.append(course)