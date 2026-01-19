def is_free_at(self, check_time):
    """
    cambia el formato de tiempo a '%H:%M' y verifica si hay disponibilidad en el aula.
    :param check_time: str, el tiempo que necesita ser verificado
    :return: True si el check_time no entra en conflicto con el horario de ningún curso, o False en caso contrario.
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.is_free_at('10:00')
    True
    >>> classroom.is_free_at('9:00')
    False
    """
    from datetime import datetime
    
    # Normalizar el formato del tiempo de verificación
    check_time_parts = check_time.split(':')
    if len(check_time_parts[0]) == 1:
        check_time = '0' + check_time
    
    # Convertir check_time a objeto datetime para comparación
    check_dt = datetime.strptime(check_time, '%H:%M')
    
    # Verificar si hay conflicto con algún curso
    for course in self.courses:
        # Normalizar start_time y end_time
        start_time = course['start_time']
        end_time = course['end_time']
        
        start_parts = start_time.split(':')
        if len(start_parts[0]) == 1:
            start_time = '0' + start_time
            
        end_parts = end_time.split(':')
        if len(end_parts[0]) == 1:
            end_time = '0' + end_time
        
        # Convertir a datetime
        start_dt = datetime.strptime(start_time, '%H:%M')
        end_dt = datetime.strptime(end_time, '%H:%M')
        
        # Verificar si check_time está dentro del rango [start_time, end_time)
        if start_dt <= check_dt < end_dt:
            return False
    
    return True