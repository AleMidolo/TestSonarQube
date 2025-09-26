from datetime import datetime


class Classroom:
    def __init__(self, id):
        self.id = id
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        check_time = self._parse_time(check_time)
        return all(not self._is_time_conflicted(course, check_time) for course in self.courses)

    def check_course_conflict(self, new_course):
        new_start_time = self._parse_time(new_course['start_time'])
        new_end_time = self._parse_time(new_course['end_time'])

        return not any(self._is_time_conflicted(course, new_start_time, new_end_time) for course in self.courses)

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, '%H:%M')

    def _is_time_conflicted(self, course, check_time, end_time=None):
        start_time = self._parse_time(course['start_time'])
        end_time = end_time or self._parse_time(course['end_time'])
        return start_time <= check_time <= end_time