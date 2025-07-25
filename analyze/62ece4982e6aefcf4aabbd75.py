import subprocess

def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    try:
        # Get the list of ignored files using git
        result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        ignored_files = result.stdout.strip().split('\n')
        
        # Sort the list of ignored files
        ignored_files = sorted(set(ignored_files))
        
        # Join the list into a single string separated by commas
        return ', '.join(ignored_files)
    except Exception as e:
        return str(e)