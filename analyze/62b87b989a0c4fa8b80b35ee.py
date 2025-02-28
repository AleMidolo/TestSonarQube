def reset(self):
    """
    Reset the histogram.

    Current context is reset to an empty dict.
    Bins are reinitialized with the *initial_value*
    or with *make_bins()* (depending on the initialization).
    """
    self.current_context = {}
    if hasattr(self, 'initial_value'):
        self.bins = [self.initial_value] * len(self.bins)
    else:
        self.bins = self.make_bins()