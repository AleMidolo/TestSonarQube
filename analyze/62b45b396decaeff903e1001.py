def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    if not params:
        params = {}
        
    if bug_ids:
        if isinstance(bug_ids, (list, tuple)):
            params['bug_id'] = bug_ids
        else:
            params['bug_id'] = [bug_ids]
            
    if 'include_fields' not in params:
        params['include_fields'] = ['id', 'summary', 'status', 'resolution', 
                                  'product', 'component', 'version', 'platform',
                                  'whiteboard', 'keywords', 'assigned_to',
                                  'creator', 'creation_time', 'last_change_time']
                                  
    if 'exclude_fields' not in params:
        params['exclude_fields'] = ['description', 'cc', 'comments', 'history']
        
    return params