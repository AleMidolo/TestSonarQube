def get_all_major(self):
    """
        obtener todas las carreras en el sistema
        :return una lista de especialidades
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}]
        >>> registration_system.get_all_major()
        ["Computer Science"]
        """
    return list(set((student['major'] for student in self.students)))