def register_student(self, student):
    """
        registrar un estudiante en el sistema, agregar el estudiante a la lista de estudiantes, si el estudiante ya está registrado, retornar 0, de lo contrario retornar 1
        """
    for existing_student in self.students:
        if existing_student['name'] == student['name']:
            return 0
    self.students.append(student)
    return 1