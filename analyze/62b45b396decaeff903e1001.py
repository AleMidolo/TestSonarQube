def amend_bzparams(self, params, bug_ids):
    """Modifica i parametri di Bugzilla"""
    for bug_id in bug_ids:
        if bug_id in params:
            params[bug_id]['status'] = 'modified'
            # Add any additional modifications needed for Bugzilla parameters
    return params