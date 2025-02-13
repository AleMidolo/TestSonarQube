def setdefault(self, key, default=None):
    if key in self:
        return self[key]
    else:
        self[key] = default
        return default