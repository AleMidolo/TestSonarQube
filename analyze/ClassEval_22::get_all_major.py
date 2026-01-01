def get_all_major(self):
    """
        ottieni tutte le specializzazioni nel sistema
        :return una lista di specializzazioni
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}]
        >>> registration_system.get_all_major()
        ["Computer Science"]
        """
    return list(set((student['major'] for student in self.students)))