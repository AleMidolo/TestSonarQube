def get_top_student(self):
    """
    प्रत्येक छात्र का GPA get_gpa विधि के साथ गणना करें, और सबसे उच्च GPA वाले छात्र को खोजें
    :return: str, उस छात्र का नाम जिसका GPA सबसे उच्च है
    >>> system.add_student('student 1', 3, 'SE')
    >>> system.add_student('student 2', 2, 'SE')
    >>> system.add_course_score('student 1', 'Computer Network', 92)
    >>> system.add_course_score('student 2', 'Computer Network', 97)
    >>> system.get_top_student()
    'student 2'
    """
    if not self.students:
        return None
    
    top_student = None
    highest_gpa = -1
    
    for student_name in self.students:
        gpa = self.get_gpa(student_name)
        if gpa > highest_gpa:
            highest_gpa = gpa
            top_student = student_name
    
    return top_student