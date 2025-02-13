def _update_context(self, context):
    error_indices = []
    for index, error in enumerate(self.errors):
        if error:
            error_indices.append(index)
    
    context['error'] = {}
    if 'x' not in context['error']:
        context['error']['x'] = {}
    context['error']['x']['index'] = error_indices

    # Assuming self.fields contains the relevant fields of the graph
    for field in self.fields:
        if field not in context:
            context[field] = {}
        context[field].update(self.get_field_properties(field))