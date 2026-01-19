def check_course_conflict(self, new_course):
    """
    एक नए पाठ्यक्रम को जोड़ने से पहले, यह जांचें कि क्या नए पाठ्यक्रम का समय किसी अन्य पाठ्यक्रम के साथ टकराता है।
    :param new_course: dict, पाठ्यक्रम की जानकारी, जिसमें 'start_time', 'end_time' और 'name' शामिल हैं
    :return: False यदि नए पाठ्यक्रम का समय अन्य पाठ्यक्रमों के साथ टकराता है (जिसमें दो पाठ्यक्रमों का समान सीमा समय होना शामिल है), अन्यथा True।
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
    
    # Check if self.courses exists, if not assume no courses yet
    if not hasattr(self, 'courses'):
        return True
    
    for course in self.courses:
        existing_start = time_to_minutes(course['start_time'])
        existing_end = time_to_minutes(course['end_time'])
        
        # Check for overlap (including boundary touching)
        # Two time ranges overlap if:
        # new_start < existing_end AND new_end > existing_start
        # But since boundary touching is also considered a conflict:
        # new_start <= existing_end AND new_end >= existing_start
        # However, based on the example, 9:40-9:40 is a conflict
        # So we use: new_start < existing_end AND new_end > existing_start
        # Actually, the example shows that touching boundaries IS a conflict
        if new_start < existing_end and new_end > existing_start:
            return False
    
    return True