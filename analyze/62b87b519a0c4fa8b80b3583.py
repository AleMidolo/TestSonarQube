def scale(self, other=None):
    """
    Get or set the scale of the graph.

    If *other* is ``None``, return the scale of this graph.

    If a numeric *other* is provided, rescale to that value.
    If the graph has unknown or zero scale,
    rescaling that will raise :exc:`~.LenaValueError`.

    To get meaningful results, graph's fields are used.
    Only the last coordinate is rescaled.
    For example, if the graph has *x* and *y* coordinates,
    then *y* will be rescaled, and for a 3-dimensional graph
    *z* will be rescaled.
    All errors are rescaled together with their coordinate.
    """
    if other is None:
        return self.scale_value  # Assuming self.scale_value holds the current scale

    if self.scale_value is None or self.scale_value == 0:
        raise LenaValueError("Cannot rescale with unknown or zero scale.")

    # Assuming self.coordinates is a list of coordinates
    last_coordinate_index = len(self.coordinates) - 1
    self.coordinates[last_coordinate_index] *= other / self.scale_value
    self.scale_value = other

    # Rescale errors if they exist
    if hasattr(self, 'errors'):
        for error in self.errors:
            error[last_coordinate_index] *= other / self.scale_value