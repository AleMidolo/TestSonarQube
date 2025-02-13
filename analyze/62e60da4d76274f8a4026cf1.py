def values(self, *keys):
    if not keys:
        return list(self.index.values())
    return [self.index[key] for key in keys if key in self.index]