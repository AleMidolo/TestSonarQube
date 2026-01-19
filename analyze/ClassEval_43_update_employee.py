def update_employee(self, employee_id: int, employee_info: dict):
    """
    Aggiorna le informazioni di un dipendente nel sistema di gestione HR.
    :param employee_id: L'id del dipendente, int.
    :param employee_info: Le informazioni del dipendente, dict.
    :return: Se il dipendente è già nel sistema di gestione HR, restituisce True, altrimenti restituisce False.
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
    >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
    True
    >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
    False

    """
    if employee_id in self.employees:
        self.employees[employee_id] = employee_info
        return True
    else:
        return False