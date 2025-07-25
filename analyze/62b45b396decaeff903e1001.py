def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    if not isinstance(params, dict):
        raise ValueError("params must be a dictionary")
    if not isinstance(bug_ids, (list, int)):
        raise ValueError("bug_ids must be a list or an integer")
    
    if isinstance(bug_ids, int):
        bug_ids = [bug_ids]
    
    params['id'] = bug_ids
    return params