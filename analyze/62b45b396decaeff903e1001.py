def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    for bug_id in bug_ids:
        # Assuming `self.bz` is a Bugzilla client object
        self.bz.update_bug(bug_id, params)