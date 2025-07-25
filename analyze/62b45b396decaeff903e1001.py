def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    if not params:
        params = {}
        
    if bug_ids:
        if isinstance(bug_ids, (list, tuple)):
            params['ids'] = bug_ids
        else:
            params['ids'] = [bug_ids]
            
    if 'include_fields' not in params:
        params['include_fields'] = ['id', 'summary', 'status', 'resolution']
        
    if 'exclude_fields' not in params:
        params['exclude_fields'] = ['description']
        
    return params