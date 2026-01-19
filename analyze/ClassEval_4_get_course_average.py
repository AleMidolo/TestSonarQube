def get_course_average(self, course):
    """
    获取特定课程的平均分数。
    :param course: 字符串，课程名称
    :return: float，如果有人有该课程的分数，则返回该课程的平均分数；如果没有人有记录,则返回 None。
    """
    total_score = 0
    count = 0
    
    for student in self.students.values():
        if course in student.grades:
            total_score += student.grades[course]
            count += 1
    
    if count == 0:
        return None
    
    return total_score / count