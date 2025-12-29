def get_all_major(self):
    """
        सिस्टम में सभी मेजर्स प्राप्त करें
        :return मेजर्स की एक सूची
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}]
        >>> registration_system.get_all_major()
        ["Computer Science"]
        """
    return list(set((student['major'] for student in self.students)))