def amend_bzparams(self, params, bug_ids):
    """Modifica i parametri di Bugzilla"""
    if not params:
        params = {}
    
    # Convert single bug_id to list if needed
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    elif bug_ids:
        bug_ids = [str(b) for b in bug_ids]
        
    # Add bug IDs to parameters if provided
    if bug_ids:
        params['ids'] = bug_ids
        
    # Ensure include_fields is a list
    if 'include_fields' in params and isinstance(params['include_fields'], str):
        params['include_fields'] = [params['include_fields']]
        
    # Ensure exclude_fields is a list  
    if 'exclude_fields' in params and isinstance(params['exclude_fields'], str):
        params['exclude_fields'] = [params['exclude_fields']]
        
    return params