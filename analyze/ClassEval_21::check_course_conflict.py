def check_course_conflict(self, new_course):
    """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
    new_start = datetime.strptime(new_course['start_time'], '%H:%M')
    new_end = datetime.strptime(new_course['end_time'], '%H:%M')
    for course in self.courses:
        start = datetime.strptime(course['start_time'], '%H:%M')
        end = datetime.strptime(course['end_time'], '%H:%M')
        if not (new_end <= start or new_start >= end):
            return False
    return True