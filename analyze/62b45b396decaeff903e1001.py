def amend_bzparams(self, params, bug_ids):
    """Modifica i parametri di Bugzilla"""
    for bug_id in bug_ids:
        if bug_id in params:
            params[bug_id] = self.modify_param(params[bug_id])
    return params

def modify_param(self, param):
    # Example modification logic
    return param + "_modified"