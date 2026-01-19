def get_gpa(self, name):
    """
        एक छात्र का औसत ग्रेड प्राप्त करें।
        :param name: str, छात्र का नाम
        :return: यदि नाम छात्रों में है और इस छात्र के पास पाठ्यक्रम का ग्रेड है, तो औसत ग्रेड (float) लौटाएं
                    अन्यथा None लौटाएं
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0
        """
    if name in self.students:
        courses = self.students[name]['courses']
        if courses:
            return sum(courses.values()) / len(courses)
    return None