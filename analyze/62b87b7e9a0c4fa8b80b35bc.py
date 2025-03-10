def _update_context(self, context):
    """
    Update *context* with the properties of this graph.

    *context.error* is appended with indices of errors.
    Example subcontext for a graph with fields "E,t,error_E_low":
    {"error": {"x_low": {"index": 2}}}.
    Note that error names are called "x", "y" and "z"
    (this corresponds to first three coordinates,
    if they are present), which allows to simplify plotting.
    Existing values are not removed
    from *context.value* and its subcontexts.

    Called on "destruction" of the graph (for example,
    in :class:`.ToCSV`). By destruction we mean conversion
    to another structure (like text) in the flow.
    The graph object is not really destroyed in this process.
    """
    if not hasattr(context, 'error'):
        context.error = {}
    
    # Assuming self has a property 'errors' that contains the error indices
    if hasattr(self, 'errors'):
        for error_name, error_index in self.errors.items():
            if error_name in ['x', 'y', 'z']:
                context.error[f"{error_name}_low"] = {"index": error_index}
    
    # Ensure existing values in context.value are not removed
    if not hasattr(context, 'value'):
        context.value = {}