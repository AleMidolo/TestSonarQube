def remove_course(self, course):
    """
        यदि पाठ्यक्रम self.courses सूची में था, तो उसे हटा दें।
        :param course: dict, पाठ्यक्रम की जानकारी, जिसमें 'start_time', 'end_time' और 'name' शामिल हैं
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
    if course in self.courses:
        self.courses.remove(course)