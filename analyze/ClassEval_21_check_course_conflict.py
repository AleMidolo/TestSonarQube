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
    def time_to_minutes(time_str):
        """将时间字符串转换为分钟数"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    new_start = time_to_minutes(new_course['start_time'])
    new_end = time_to_minutes(new_course['end_time'])
    
    # 检查是否有courses属性，如果没有则返回True（没有冲突）
    if not hasattr(self, 'courses'):
        return True
    
    # 检查与现有课程的冲突
    for course in self.courses:
        existing_start = time_to_minutes(course['start_time'])
        existing_end = time_to_minutes(course['end_time'])
        
        # 检查时间冲突（包括边界时间相同的情况）
        # 如果新课程的开始时间在现有课程的时间范围内（包括边界）
        # 或者新课程的结束时间在现有课程的时间范围内（包括边界）
        # 或者新课程完全包含现有课程
        if not (new_end <= existing_start or new_start >= existing_end):
            return False
    
    return True