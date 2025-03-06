def amend_bzparams(self, params, bug_ids):
    """
    बगज़िला पैरामीटर्स को संशोधित करें
    """
    for bug_id in bug_ids:
        if bug_id in params:
            # Modify the parameters for the given bug ID
            params[bug_id] = {
                'status': 'MODIFIED',
                'comment': 'Parameters have been amended.'
            }
        else:
            # Add new parameters for the given bug ID
            params[bug_id] = {
                'status': 'NEW',
                'comment': 'New parameters added.'
            }
    return params