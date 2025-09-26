class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if self._employee_exists(employee_id):
            return False
        self.employees[employee_id] = self._create_employee_record(name, position, department, salary)
        return True

    def remove_employee(self, employee_id):
        if self._employee_exists(employee_id):
            del self.employees[employee_id]
            return True
        return False

    def update_employee(self, employee_id: int, employee_info: dict):
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        if not self._is_valid_update(employee_info, employee):
            return False
        self._update_employee_info(employee, employee_info)
        return True

    def get_employee(self, employee_id):
        return self.employees.get(employee_id, False)

    def list_employees(self):
        return {employee_id: self._format_employee_details(employee_id, employee_info) 
                for employee_id, employee_info in self.employees.items()}

    def _employee_exists(self, employee_id):
        return employee_id in self.employees

    def _create_employee_record(self, name, position, department, salary):
        return {
            'name': name,
            'position': position,
            'department': department,
            'salary': salary
        }

    def _is_valid_update(self, employee_info, employee):
        return all(key in employee for key in employee_info)

    def _update_employee_info(self, employee, employee_info):
        for key, value in employee_info.items():
            employee[key] = value

    def _format_employee_details(self, employee_id, employee_info):
        employee_details = {"employee_ID": employee_id}
        employee_details.update(employee_info)
        return employee_details