def remove_course(self, course):
    """
    如果课程在 self.courses 列表中，则从中移除课程。
    :param course: dict，课程的信息，包括 'start_time'，'end_time' 和 'name'
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    """
    if course in self.courses:
        self.courses.remove(course)