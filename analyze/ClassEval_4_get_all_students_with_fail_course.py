def get_all_students_with_fail_course(self):
    """
    उन सभी छात्रों को प्राप्त करें जिनका कोई भी स्कोर 60 से कम है
    :return: str की सूची, छात्र का नाम
    >>> system.add_course_score('student 1', 'Society', 59)
    >>> system.get_all_students_with_fail_course()
    ['student 1']
    """
    students_with_fail = []
    
    for student_name, courses in self.students.items():
        for course_name, score in courses.items():
            if score < 60:
                students_with_fail.append(student_name)
                break
    
    return students_with_fail