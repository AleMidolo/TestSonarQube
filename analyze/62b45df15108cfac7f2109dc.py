def status_str(self, prefix=''):
    return ''.join(f"{prefix}{message}" for message in sorted(self.messages))