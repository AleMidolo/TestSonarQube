def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    for bug_id in bug_ids:
        params[f'bug_id_{bug_id}'] = True
    return params