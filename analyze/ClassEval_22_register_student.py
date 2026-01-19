def register_student(self, student):
    """
    सिस्टम में एक छात्र को पंजीकृत करें, छात्र को छात्रों की सूची में जोड़ें, यदि छात्र पहले से पंजीकृत है, तो 0 लौटाएं, अन्यथा 1 लौटाएं
    """
    if student in self.students:
        return 0
    else:
        self.students.append(student)
        return 1