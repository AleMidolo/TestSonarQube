def get_course_average(self, course):
    """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
    scores = []
    for student in self.students.values():
        if course in student['courses']:
            scores.append(student['courses'][course])
    if scores:
        return sum(scores) / len(scores)
    else:
        return None