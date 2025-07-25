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
            
    if 'ids' in params and not params['ids']:
        del params['ids']
        
    return params