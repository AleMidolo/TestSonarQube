class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        if self._student_exists(name):
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        if self._student_exists(name) and self._has_courses(name):
            return self._calculate_gpa(name)
        return None

    def get_all_students_with_fail_course(self):
        return [name for name, student in self.students.items() if self._has_failed_course(student)]

    def get_course_average(self, course):
        total, count = self._calculate_course_average(course)
        return total / count if count > 0 else None

    def get_top_student(self):
        top_student, top_gpa = self._find_top_student()
        return top_student

    def _student_exists(self, name):
        return name in self.students

    def _has_courses(self, name):
        return bool(self.students[name]['courses'])

    def _calculate_gpa(self, name):
        return sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])

    def _has_failed_course(self, student):
        return any(score < 60 for score in student['courses'].values())

    def _calculate_course_average(self, course):
        total = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                score = student['courses'][course]
                if score is not None:
                    total += score
                    count += 1
        return total, count

    def _find_top_student(self):
        top_student = None
        top_gpa = 0
        for name, student in self.students.items():
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > top_gpa:
                top_gpa = gpa
                top_student = name
        return top_student, top_gpa