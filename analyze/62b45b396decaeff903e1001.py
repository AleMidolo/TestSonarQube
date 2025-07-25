def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    for bug_id in bug_ids:
        if bug_id in params:
            params[bug_id]['status'] = 'modified'
            # Add any other modifications needed for Bugzilla parameters
    return params