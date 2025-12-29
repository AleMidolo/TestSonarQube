def get_all_students_with_fail_course(self):
    """
        Ottieni tutti gli studenti che hanno un punteggio inferiore a 60
        :return: lista di str, nome dello studente
        >>> system.add_course_score('studente 1', 'Società', 59)
        >>> system.get_all_students_with_fail_course()
        ['studente 1']
        """
    failing_students = []
    for name, student in self.students.items():
        for course, score in student['courses'].items():
            if score < 60:
                failing_students.append(name)
                break
    return failing_students