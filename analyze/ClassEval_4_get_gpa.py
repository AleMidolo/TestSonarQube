def get_gpa(self, name):
    """
    Ottieni la media dei voti di uno studente.
    :param name: str, nome dello studente
    :return: se il nome è presente negli studenti e questo studente ha voti nei corsi, restituisce la media dei voti (float)
                altrimenti restituisce None
    >>> system.add_student('student 1', 3, 'SE')
    >>> system.add_course_score('student 1', 'math', 94)
    >>> system.add_course_score('student 1', 'Computer Network', 92)
    >>> system.get_gpa('student 1')
    93.0

    """
    # Check if student exists
    if name not in self.students:
        return None
    
    # Get the student's course scores
    student = self.students[name]
    
    # Check if student has a courses/scores attribute and if it has any scores
    if not hasattr(student, 'courses') or not student.courses:
        return None
    
    # Calculate the average of all course scores
    total_score = sum(student.courses.values())
    num_courses = len(student.courses)
    
    if num_courses == 0:
        return None
    
    return float(total_score / num_courses)