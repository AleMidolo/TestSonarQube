from datetime import datetime

class Classroom: 
    def __init__(self, id):
        """
        Initialize the classroom management system.
        :param id: int, the id of classroom
        """
        self.id = id
        self.courses = []

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
        check_time = datetime.strptime(check_time, '%H:%M')

        for course in self.courses:
            if datetime.strptime(course['start_time'], '%H:%M') <= check_time <= datetime.strptime(course['end_time'], '%H:%M'):
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Prima di aggiungere un nuovo corso, controlla se l'orario del nuovo corso  è in conflitto con altri corsi.
        :param new_course: dict, informazioni del corso, inclusi 'start_time', 'end_time' e 'name'
        :return: False se l'orario del nuovo corso confligge (incluso il caso in cui due corsi abbiano lo stesso orario di confine) con altri corsi, o True altrimenti.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
        new_start = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end = datetime.strptime(new_course['end_time'], '%H:%M')

        for course in self.courses:
            course_start = datetime.strptime(course['start_time'], '%H:%M')
            course_end = datetime.strptime(course['end_time'], '%H:%M')
            if not (new_end <= course_start or new_start >= course_end):
                return False
        return True