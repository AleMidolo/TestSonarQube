def get_all_students_with_fail_course(self):
    """
    获取所有有任何分数低于60的学生
    :return: 字符串的列表，学生姓名
    >>> system.add_course_score('student 1', 'Society', 59)
    >>> system.get_all_students_with_fail_course()
    ['student 1']
    """
    students_with_fail = []
    
    # Iterate through all students and their courses
    for student_name, courses in self.students.items():
        # Check if any course score is below 60
        for course_name, score in courses.items():
            if score < 60:
                students_with_fail.append(student_name)
                break  # No need to check other courses for this student
    
    return students_with_fail