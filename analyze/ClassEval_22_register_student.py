def register_student(self, student):
    """
    将学生注册到系统中，将学生添加到学生列表中，如果学生已经注册，则返回0，否则返回1
    """
    if not hasattr(self, 'students'):
        self.students = []
    
    # 检查学生是否已经注册
    for existing_student in self.students:
        if existing_student == student:
            return 0
    
    # 添加学生到列表
    self.students.append(student)
    return 1