def check_course_conflict(self, new_course):
    """
    Before adding a new course, check if the new course time conflicts with any other course.
    :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
    :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
    False
    """
    def time_to_minutes(time_str):
        """Convert time string 'HH:MM' to minutes since midnight"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    new_start = time_to_minutes(new_course['start_time'])
    new_end = time_to_minutes(new_course['end_time'])
    
    # Check against all existing courses
    for course in self.courses:
        existing_start = time_to_minutes(course['start_time'])
        existing_end = time_to_minutes(course['end_time'])
        
        # Check if there's any overlap (including boundary times)
        # Conflict occurs if:
        # - new course starts before existing ends AND new course ends after existing starts
        if new_start < existing_end and new_end > existing_start:
            return False
    
    return True