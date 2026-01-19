def add_course(self, course):
    """
        如果课程不在 self.courses 列表中，则将课程添加到该列表中。
        :param course: dict，课程信息，包括 'start_time'，'end_time' 和 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
    if not self.check_course_conflict(course):
        return
    if course not in self.courses:
        self.courses.append(course)