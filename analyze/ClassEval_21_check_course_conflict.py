def check_course_conflict(self, new_course):
    """
    Antes de agregar un nuevo curso, verifica si el horario del nuevo curso entra en conflicto con algún otro curso.
    :param new_course: dict, información del curso, incluyendo 'start_time', 'end_time' y 'name'
    :return: False si el horario del nuevo curso entra en conflicto (incluyendo si dos cursos tienen el mismo tiempo límite) con otros cursos, o True en caso contrario.
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
    False
    """
    new_start = new_course['start_time']
    new_end = new_course['end_time']
    
    # Check against all existing courses
    for course in self.courses:
        existing_start = course['start_time']
        existing_end = course['end_time']
        
        # Check if there's any overlap or touching boundaries
        # Conflict occurs if:
        # 1. New course starts before existing ends AND new course ends after existing starts
        # 2. Including when boundaries touch (same time limit)
        if not (new_end <= existing_start or new_start >= existing_end):
            return False
    
    return True