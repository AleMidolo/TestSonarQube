def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    if not isinstance(params, dict):
        raise ValueError("params must be a dictionary")
    if not isinstance(bug_ids, (list, int)):
        raise ValueError("bug_ids must be a list or an integer")
    
    if isinstance(bug_ids, int):
        bug_ids = [bug_ids]
    
    for bug_id in bug_ids:
        if not isinstance(bug_id, int):
            raise ValueError("bug_ids must contain integers only")
    
    # Assuming self.bz is the Bugzilla client object
    for bug_id in bug_ids:
        self.bz.update_bugs(bug_id, params)