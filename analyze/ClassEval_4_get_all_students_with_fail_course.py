def get_all_students_with_fail_course(self):
    """
    Ottieni tutti gli studenti che hanno un punteggio inferiore a 60
    :return: lista di str, nome dello studente
    >>> system.add_course_score('studente 1', 'Società', 59)
    >>> system.get_all_students_with_fail_course()
    ['studente 1']
    """
    students_with_fail = []
    
    # Assuming self has a data structure to store student scores
    # Common patterns: self.students, self.scores, self.course_scores
    if hasattr(self, 'course_scores'):
        for student, courses in self.course_scores.items():
            for course, score in courses.items():
                if score < 60:
                    if student not in students_with_fail:
                        students_with_fail.append(student)
                    break
    elif hasattr(self, 'students'):
        for student, data in self.students.items():
            if isinstance(data, dict) and 'courses' in data:
                for course, score in data['courses'].items():
                    if score < 60:
                        if student not in students_with_fail:
                            students_with_fail.append(student)
                        break
    
    return students_with_fail