def amend_bzparams(self, params, bug_ids):
    """Modifica i parametri di Bugzilla"""
    if not params:
        params = {}
    
    # Convert single bug ID to list if needed
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    elif bug_ids:
        bug_ids = [str(bid) for bid in bug_ids]
        
    # Add bug IDs to parameters if provided
    if bug_ids:
        params['ids'] = bug_ids
        
    # Add include_fields if not present
    if 'include_fields' not in params:
        params['include_fields'] = ['id', 'summary', 'status']
        
    # Add other common parameters if not present
    if 'exclude_fields' not in params:
        params['exclude_fields'] = ['description']
        
    return params