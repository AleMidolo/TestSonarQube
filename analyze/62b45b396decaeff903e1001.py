def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    if not params:
        params = {}
    
    # Convert single bug_id to list if needed
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    elif bug_ids:
        bug_ids = [str(bug_id) for bug_id in bug_ids]
        
    # Add bug IDs to parameters if provided
    if bug_ids:
        params['ids'] = bug_ids
        
    # Ensure include_fields is a list
    if 'include_fields' in params and isinstance(params['include_fields'], str):
        params['include_fields'] = [params['include_fields']]
        
    # Add default fields if not specified
    if 'include_fields' not in params:
        params['include_fields'] = ['id', 'summary', 'status']
        
    return params