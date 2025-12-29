def register_student(self, student):
    """
        registra uno studente nel sistema, aggiunge lo studente alla lista degli studenti, se lo studente è già registrato, restituisce 0, altrimenti restituisce 1
        """
    if any((s['name'] == student['name'] for s in self.students)):
        return 0
    else:
        self.students.append(student)
        return 1