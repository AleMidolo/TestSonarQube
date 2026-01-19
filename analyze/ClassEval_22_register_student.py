def register_student(self, student):
    """
        将学生注册到系统中，将学生添加到学生列表中，如果学生已经注册，则返回0，否则返回1
        """
    if student in self.students:
        return 0
    else:
        self.students.append(student)
        return 1