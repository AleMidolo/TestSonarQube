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
    
    check_time_dt = datetime.strptime(check_time, '%H:%M')
    
    for course in self.courses:
        start_time = datetime.strptime(course['start_time'], '%H:%M')
        end_time = datetime.strptime(course['end_time'], '%H:%M')
        if start_time <= check_time_dt <= end_time:
            return False
    return True