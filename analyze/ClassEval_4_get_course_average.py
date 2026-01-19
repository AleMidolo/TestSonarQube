def get_course_average(self, course):
    """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if someone has a score for this course, or None if no one has records.
        """
    total_score = 0
    count = 0
    for student in self.students.values():
        if course in student['courses']:
            total_score += student['courses'][course]
            count += 1
    return total_score / count if count > 0 else None