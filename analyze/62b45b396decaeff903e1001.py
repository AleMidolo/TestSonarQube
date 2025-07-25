def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    if not isinstance(params, dict):
        raise ValueError("params must be a dictionary")
    if not isinstance(bug_ids, (list, tuple)):
        raise ValueError("bug_ids must be a list or tuple")
    
    params['id'] = bug_ids
    return params