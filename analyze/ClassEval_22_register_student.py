def register_student(self, student):
    """
        सिस्टम में एक छात्र को पंजीकृत करें, छात्र को छात्रों की सूची में जोड़ें, यदि छात्र पहले से पंजीकृत है, तो 0 लौटाएं, अन्यथा 1 लौटाएं
        """
    for s in self.students:
        if s['name'] == student['name']:
            return 0
    self.students.append(student)
    return 1