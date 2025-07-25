def amend_bzparams(self, params, bug_ids):
    """
    修改 Bugzilla 参数
    """
    # 假设我们有一个 Bugzilla API 客户端实例 self.bz
    # 遍历每个 bug_id 并更新参数
    for bug_id in bug_ids:
        self.bz.update_bug(bug_id, params)