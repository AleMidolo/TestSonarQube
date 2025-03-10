def amend_bzparams(self, params, bug_ids):
    """
    बगज़िला पैरामीटर्स को संशोधित करें
    """
    # Assuming params is a dictionary and bug_ids is a list of bug IDs
    # Modify the params dictionary to include the bug IDs
    if 'bug_ids' not in params:
        params['bug_ids'] = []
    params['bug_ids'].extend(bug_ids)
    return params