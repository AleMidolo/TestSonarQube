def remove_course(self, course):
    """
        Elimina el curso de la lista self.courses si el curso estaba en ella.
        :param course: dict, información del curso, incluyendo 'start_time', 'end_time' y 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.remove_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.courses
        []
        """
    if course in self.courses:
        self.courses.remove(course)