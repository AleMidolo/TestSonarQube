def get_course_average(self, course):
    """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
    total_score = 0
    count = 0
    for student in self.students.values():
        if course in student['courses']:
            total_score += student['courses'][course]
            count += 1
    if count > 0:
        return total_score / count
    else:
        return None