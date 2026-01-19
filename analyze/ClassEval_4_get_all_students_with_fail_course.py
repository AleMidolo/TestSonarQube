def get_all_students_with_fail_course(self):
    """
    Get all students who have any score blow 60
    :return: list of str ,student name
    >>> system.add_course_score('student 1', 'Society', 59)
    >>> system.get_all_students_with_fail_course()
    ['student 1']
    """
    failing_students = []
    
    # Iterate through all students and their scores
    for student_name, courses in self.students.items():
        # Check if any course score is below 60
        for course_name, score in courses.items():
            if score < 60:
                failing_students.append(student_name)
                break  # No need to check other courses for this student
    
    return failing_students