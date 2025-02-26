def amend_bzparams(self, params, bug_ids):
    """
    修改 Bugzilla 参数
    """
    for bug_id in bug_ids:
        if bug_id in params:
            params[bug_id]['status'] = 'amended'
            params[bug_id]['updated'] = True
    return params