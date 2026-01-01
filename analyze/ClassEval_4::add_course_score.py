def add_course_score(self, name, course, score):
    """
        विशेष पाठ्यक्रम के लिए छात्र का स्कोर self.students में जोड़ें
        :param name: str, छात्र का नाम
        :param course: str, पाठ्यक्रम का नाम
        :param score: int, पाठ्यक्रम का स्कोर
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
    if name in self.students:
        self.students[name]['courses'][course] = score