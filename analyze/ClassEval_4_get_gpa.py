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
    # Check if student exists in the system
    if name not in self.students:
        return None
    
    # Get the student's course scores
    student = self.students[name]
    
    # Check if student has a courses/scores attribute and if it has any grades
    if hasattr(student, 'courses') and student.courses:
        scores = list(student.courses.values())
        if scores:
            return float(sum(scores) / len(scores))
        else:
            return None
    elif hasattr(student, 'scores') and student.scores:
        scores = list(student.scores.values())
        if scores:
            return float(sum(scores) / len(scores))
        else:
            return None
    else:
        return None