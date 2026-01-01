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
    if name not in self.students:
        return None
    student = self.students[name]
    courses = student['courses']
    if not courses:
        return None
    total = sum(courses.values())
    count = len(courses)
    return total / count