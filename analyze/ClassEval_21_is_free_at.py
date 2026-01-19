def is_free_at(self, check_time):
    """
    将时间格式更改为 '%H:%M' 并检查教室在该时间是否空闲。
    :param check_time: str, 需要检查的时间
    :return: 如果 check_time 与所有课程时间没有冲突,则返回 True,否则返回 False。
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.is_free_at('10:00')
    True
    >>> classroom.is_free_at('9:00')
    False
    """
    from datetime import datetime
    
    # 将检查时间转换为标准格式
    check_time_obj = datetime.strptime(check_time, '%H:%M')
    
    # 遍历所有课程,检查是否有时间冲突
    for course in self.courses:
        start_time_obj = datetime.strptime(course['start_time'], '%H:%M')
        end_time_obj = datetime.strptime(course['end_time'], '%H:%M')
        
        # 如果检查时间在课程的开始时间(含)和结束时间(不含)之间,则不空闲
        if start_time_obj <= check_time_obj < end_time_obj:
            return False
    
    # 如果没有冲突,则空闲
    return True