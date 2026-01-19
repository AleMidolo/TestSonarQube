def remove_employee(self, employee_id):
    """
    Rimuovi un dipendente dal HRManagementSystem.
    :param employee_id: L'id del dipendente, int.
    :return: Se il dipendente è già nel HRManagementSystem, restituisce True, altrimenti restituisce False.
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
    >>> hrManagementSystem.remove_employee(1)
    True
    >>> hrManagementSystem.remove_employee(2)
    False

    """
    if employee_id in self.employees:
        del self.employees[employee_id]
        return True
    else:
        return False