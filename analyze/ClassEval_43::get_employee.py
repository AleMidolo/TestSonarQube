def get_employee(self, employee_id):
    """
        Ottieni le informazioni di un dipendente dal HRManagementSystem.
        :param employee_id: L'id del dipendente, int.
        :return: Se il dipendente è già nel HRManagementSystem, restituisce le informazioni del dipendente, altrimenti restituisce False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.get_employee(1)
        {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        >>> hrManagementSystem.get_employee(2)
        False

        """
    if employee_id in self.employees:
        return self.employees[employee_id]
    else:
        return False