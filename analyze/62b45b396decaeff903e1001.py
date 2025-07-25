def amend_bzparams(self, params, bug_ids):
    """Modifica i parametri di Bugzilla"""
    if not isinstance(params, dict):
        raise ValueError("params must be a dictionary")
    if not isinstance(bug_ids, (list, tuple)):
        raise ValueError("bug_ids must be a list or tuple")
    
    # Assuming self.bz is the Bugzilla client instance
    for bug_id in bug_ids:
        self.bz.update_bugs(bug_id, params)