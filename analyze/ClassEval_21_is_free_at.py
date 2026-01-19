def is_free_at(self, check_time):
    """
    टाइम फ़ॉर्मेट को '%H:%M' के तौर पर बदलें और चेक करें कि क्लासरूम में दिया गया टाइम खाली है या नहीं।

    :param check_time: str, वह टाइम जिसे चेक करना है
    :return: अगर check_time हर कोर्स टाइम से नहीं टकराता है तो True, नहीं तो False

    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.is_free_at('10:00')
    True
    >>> classroom.is_free_at('9:00')
    False
    """
    from datetime import datetime
    
    # Parse the check_time
    check_dt = datetime.strptime(check_time, '%H:%M')
    
    # Check against all courses
    for course in self.courses:
        start_dt = datetime.strptime(course['start_time'], '%H:%M')
        end_dt = datetime.strptime(course['end_time'], '%H:%M')
        
        # Check if check_time falls within the course time range
        if start_dt <= check_dt < end_dt:
            return False
    
    return True