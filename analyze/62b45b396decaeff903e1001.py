def amend_bzparams(self, params, bug_ids):
    for bug_id in bug_ids:
        params[f'bug_id_{bug_id}'] = bug_id
    return params