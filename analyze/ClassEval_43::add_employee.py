def add_employee(self, employee_id, name, position, department, salary):
    """
        Aggiungi un nuovo dipendente al HRManagementSystem.
        :param employee_id: L'id del dipendente, int.
        :param name: Il nome del dipendente, str.
        :param position: La posizione del dipendente, str.
        :param department: Il dipartimento del dipendente, str.
        :param salary: Lo stipendio del dipendente, int.
        :return: Se il dipendente è già nel HRManagementSystem, restituisce False, altrimenti restituisce True.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        True
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        False

        """
    if employee_id in self.employees:
        return False
    else:
        self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
        return True