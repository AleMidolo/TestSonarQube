def register_student(self, student):
    """
        registrar un estudiante en el sistema, agregar el estudiante a la lista de estudiantes, si el estudiante ya está registrado, retornar 0, de lo contrario retornar 1
        """
    if any((s['name'] == student['name'] for s in self.students)):
        return 0
    else:
        self.students.append(student)
        return 1