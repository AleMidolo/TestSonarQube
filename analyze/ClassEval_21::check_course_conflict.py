def check_course_conflict(self, new_course):
    """
        在添加新课程之前，检查新课程的时间是否与其他课程冲突。
        :param new_course: dict，课程信息，包括 'start_time'，'end_time' 和 'name'
        :return: 如果新课程的时间与其他课程冲突（包括两个课程有相同的边界时间），则返回 False，否则返回 True。
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
    new_start = datetime.strptime(new_course['start_time'], '%H:%M')
    new_end = datetime.strptime(new_course['end_time'], '%H:%M')
    for course in self.courses:
        course_start = datetime.strptime(course['start_time'], '%H:%M')
        course_end = datetime.strptime(course['end_time'], '%H:%M')
        if not (new_end <= course_start or new_start >= course_end):
            return False
    return True