def amend_bzparams(self, params, bug_ids):
    """
    修改 Bugzilla 参数
    """
    if not params or not bug_ids:
        return params
        
    # Convert single bug_id to list
    if isinstance(bug_ids, (int, str)):
        bug_ids = [str(bug_ids)]
    else:
        bug_ids = [str(bug_id) for bug_id in bug_ids]
        
    # Add bug_ids to params
    if len(bug_ids) == 1:
        params['id'] = bug_ids[0]
    else:
        params['ids'] = ','.join(bug_ids)
        
    return params