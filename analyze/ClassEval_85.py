class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        return self.target_temperature

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        if self.is_valid_mode(mode):
            self.mode = mode
            return True
        return False

    def is_valid_mode(self, mode):
        return mode in ['heat', 'cool']

    def auto_set_mode(self):
        self.mode = 'heat' if self.current_temperature < self.target_temperature else 'cool'

    def auto_check_conflict(self):
        if self.is_conflict():
            self.auto_set_mode()
            return True
        return False

    def is_conflict(self):
        return (self.current_temperature > self.target_temperature and self.mode == 'cool') or \
               (self.current_temperature < self.target_temperature and self.mode == 'heat')

    def simulate_operation(self):
        self.auto_set_mode()
        return self.perform_simulation()

    def perform_simulation(self):
        use_time = 0
        if self.mode == 'heat':
            while self.current_temperature < self.target_temperature:
                self.current_temperature += 1
                use_time += 1
        else:
            while self.current_temperature > self.target_temperature:
                self.current_temperature -= 1
                use_time += 1
        return use_time