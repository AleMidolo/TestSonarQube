def register_student(self, student):
    """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
    if any((s['name'] == student['name'] for s in self.students)):
        return 0
    self.students.append(student)
    return 1