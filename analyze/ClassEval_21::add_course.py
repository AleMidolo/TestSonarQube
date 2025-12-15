def add_course(self, course):
    """
    यदि पाठ्यक्रम self.courses सूची में नहीं है तो पाठ्यक्रम को जोड़ें।
    :param course: dict, पाठ्यक्रम की जानकारी, जिसमें 'start_time', 'end_time' और 'name' शामिल हैं
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    """
    if not self.check_course_conflict(course):
        return  # Do not add the course if there is a conflict
    self.courses.append(course)