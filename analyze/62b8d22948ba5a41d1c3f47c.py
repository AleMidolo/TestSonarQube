def get(self, key, default=None):
    return self.data[key] if key in self.data else default