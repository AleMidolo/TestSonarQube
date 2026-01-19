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
    new_start = new_course['start_time']
    new_end = new_course['end_time']
    
    # 检查是否有courses属性，如果没有则返回True（没有冲突）
    if not hasattr(self, 'courses'):
        return True
    
    # 遍历所有已存在的课程
    for course in self.courses:
        existing_start = course['start_time']
        existing_end = course['end_time']
        
        # 检查时间冲突
        # 两个时间段冲突的条件：
        # 1. 新课程开始时间在已有课程时间范围内（包括边界）
        # 2. 新课程结束时间在已有课程时间范围内（包括边界）
        # 3. 新课程完全包含已有课程
        # 简化判断：如果两个时间段不重叠，则满足以下条件之一：
        # - 新课程结束时间 <= 已有课程开始时间
        # - 新课程开始时间 >= 已有课程结束时间
        # 因此，如果不满足上述条件，则存在冲突
        
        if not (new_end <= existing_start or new_start >= existing_end):
            return False
    
    return True