def amend_bzparams(self, params, bug_ids):
    """
    Modificar los parámetros de Bugzilla
    """
    # Assuming params is a dictionary of parameters to be updated
    # and bug_ids is a list of bug IDs to which the parameters should be applied.
    for bug_id in bug_ids:
        # Here you would typically make an API call to Bugzilla to update the parameters
        # for each bug ID. This is a placeholder for that logic.
        print(f"Updating parameters for bug {bug_id}: {params}")
        # Example API call (pseudo-code):
        # response = bugzilla_api.update_bug(bug_id, params)
        # if response.status_code != 200:
        #     raise Exception(f"Failed to update bug {bug_id}")