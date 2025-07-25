def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    # Convert single bug ID to list if needed
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    else:
        bug_ids = [str(bug_id) for bug_id in bug_ids]

    # Add bug IDs to params if not already present
    if 'ids' not in params:
        params['ids'] = bug_ids
    elif isinstance(params['ids'], (list, tuple)):
        params['ids'].extend(bug_ids)
    else:
        params['ids'] = [params['ids']] + bug_ids

    # Remove any duplicates while preserving order
    params['ids'] = list(dict.fromkeys(params['ids']))

    return params