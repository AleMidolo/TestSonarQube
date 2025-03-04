def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    # Convert single bug ID to list if needed
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    else:
        bug_ids = [str(bug_id) for bug_id in bug_ids]

    # Add bug IDs to params
    if len(bug_ids) == 1:
        params['id'] = bug_ids[0]
    else:
        params['ids'] = bug_ids

    return params