def is_free_at(self, check_time):
    """
        将时间格式更改为 '%H:%M' 并检查教室在该时间是否空闲。
        :param check_time: str, 需要检查的时间
        :return: 如果 check_time 与所有课程时间没有冲突，则返回 True，否则返回 False。
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
    check_time_dt = datetime.strptime(check_time, '%H:%M')
    for course in self.courses:
        start_time = datetime.strptime(course['start_time'], '%H:%M')
        end_time = datetime.strptime(course['end_time'], '%H:%M')
        if start_time <= check_time_dt <= end_time:
            return False
    return True