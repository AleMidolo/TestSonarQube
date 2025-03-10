def amend_bzparams(self, params, bug_ids):
    """
    修改 Bugzilla 参数
    """
    # 假设我们有一个 Bugzilla 客户端实例 self.bz_client
    for bug_id in bug_ids:
        self.bz_client.update_bug(bug_id, params)