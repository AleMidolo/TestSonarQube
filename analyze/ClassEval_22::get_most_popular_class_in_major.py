class ClassRegistrationSystem: 
    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            return 1
    
    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.register_class(student_name="John", class_name="CS101")
        >>> registration_system.register_class(student_name="John", class_name="CS102")
        ["CS101", "CS102"]
        """
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]
    
    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
        student_list = []
        for student in self.students:
            if student["major"] == major:
                student_list.append(student["name"])
        return student_list
    
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
        major_list = []
        for student in self.students:
            if student["major"] not in major_list:
                major_list.append(student["major"])
        return major_list
    
    def get_most_popular_class_in_major(self, major):
        """
        获取该专业中注册人数最多的课程。
        :return  一个字符串，表示该专业中最受欢迎课程
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "计算机科学"},
                                             {"name": "Bob", "major": "计算机科学"},
                                             {"name": "Alice", "major": "计算机科学"}]
        >>> registration_system.students_registration_classes = {"John": ["算法", "数据结构"],
                                            "Bob": ["操作系统", "数据结构", "算法"]}
        >>> registration_system.get_most_popular_class_in_major("计算机科学")
        "数据结构"
        """
        class_count = {}
        for student in self.students:
            if student["major"] == major:
                student_classes = self.students_registration_classes.get(student["name"], [])
                for class_name in student_classes:
                    if class_name in class_count:
                        class_count[class_name] += 1
                    else:
                        class_count[class_name] = 1
        if not class_count:
            return ""
        return max(class_count, key=class_count.get)