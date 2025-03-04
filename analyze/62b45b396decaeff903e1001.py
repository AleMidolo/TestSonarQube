def amend_bzparams(self, params, bug_ids):
    """
    बगज़िला पैरामीटर्स को संशोधित करें
    """
    if not bug_ids:
        return params
        
    if isinstance(bug_ids, (str, int)):
        bug_ids = [str(bug_ids)]
    else:
        bug_ids = [str(bug_id) for bug_id in bug_ids]
        
    if 'bug_id' in params:
        params['bug_id'].extend(bug_ids)
    else:
        params['bug_id'] = bug_ids
        
    return params