def is_free_at(self, check_time):
    """
    cambia il formato dell'orario in '%H:%M' e verifica se l'orario è libero o meno nell'aula.
    :param check_time: str, l'orario da controllare
    :return: True se l'orario di controllo non confligge con gli orari di nessun corso, altrimenti False.
    >>> classroom = Classroom(1)
    >>> classroom.add_course({'name': 'matematica', 'start_time': '8:00', 'end_time': '9:40'})
    >>> classroom.is_free_at('10:00')
    True
    >>> classroom.is_free_at('9:00')
    False
    """
    from datetime import datetime
    
    # Converti check_time in formato datetime per il confronto
    check_time_obj = datetime.strptime(check_time, '%H:%M')
    
    # Verifica se l'orario confligge con qualsiasi corso
    for course in self.courses:
        start_time_obj = datetime.strptime(course['start_time'], '%H:%M')
        end_time_obj = datetime.strptime(course['end_time'], '%H:%M')
        
        # Se check_time è tra start_time (incluso) e end_time (escluso), non è libero
        if start_time_obj <= check_time_obj < end_time_obj:
            return False
    
    # Se non ci sono conflitti, l'orario è libero
    return True