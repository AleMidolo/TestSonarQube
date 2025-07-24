class ClassRegistrationSystem:

    def __init__(self):
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        if self.is_student_registered(student):
            return 0
        else:
            self.students.append(student)
            return 1

    def is_student_registered(self, student):
        return student in self.students

    def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        return [student["name"] for student in self.students if student["major"] == major]

    def get_all_major(self):
        return list(set(student["major"] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        class_list = self.get_classes_by_major(major)
        return self.get_most_common_class(class_list)

    def get_classes_by_major(self, major):
        return [self.students_registration_classes[student["name"]] for student in self.students if student["major"] == major]

    def get_most_common_class(self, class_list):
        return max(set(class_list), key=class_list.count)