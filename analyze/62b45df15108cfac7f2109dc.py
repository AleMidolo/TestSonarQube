def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    # Assuming self has attributes that represent the state of the validator
    state_info = f"Validator State: {self.state}, Errors: {self.errors}, Warnings: {self.warnings}"
    return f"{prefix}{state_info}"