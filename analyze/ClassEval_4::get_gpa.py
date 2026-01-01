def get_gpa(self, name):
    """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0

        """
    if name not in self.students:
        return None
    student = self.students[name]
    courses = student['courses']
    if not courses:
        return None
    total = 0
    count = 0
    for score in courses.values():
        if score is not None:
            total += score
            count += 1
    return total / count if count > 0 else None