def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Ansible CLI को vars_dict के साथ चलाता है।

    :param vars_dict: dict, इसे Ansible extra-vars के रूप में पास किया जाएगा
    :param cli_args: कमांड लाइन आर्ग्युमेंट्स की सूची
    :param ir_workspace: एक Infrared Workspace ऑब्जेक्ट जो सक्रिय वर्कस्पेस को दर्शाता है
    :param ir_plugin: वर्तमान प्लगइन का एक InfraredPlugin ऑब्जेक्ट
    :return: ansible के परिणाम
    """
    from ansible.cli.playbook import PlaybookCLI
    from ansible import context
    from ansible.module_utils.common.collections import ImmutableDict

    # Set up Ansible context
    context.CLIARGS = ImmutableDict(cli_args)

    # Prepare extra vars
    extra_vars = vars_dict

    # Initialize PlaybookCLI
    cli = PlaybookCLI([])

    # Run the playbook
    result = cli.run()

    return result