def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: The script to be converted to a one-line command.
    :param seperator: The separator used to join the lines of the script. Default is " && ".
    :return: A single-line command string.
    """
    lines = script.strip().splitlines()
    return seperator.join(line.strip() for line in lines if line.strip())