def amend_bzparams(self, params, bug_ids):
    """
    修改 Bugzilla 参数
    """
    if not params or not bug_ids:
        return params
        
    # Convert single bug ID to list
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    else:
        bug_ids = [str(bid) for bid in bug_ids]
        
    # Add bug IDs to params
    if len(bug_ids) == 1:
        params['bug_id'] = bug_ids[0]
    else:
        params['bug_id'] = bug_ids
        
    return params