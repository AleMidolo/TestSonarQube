import subprocess

def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    ignored_files = result.stdout.strip().split('\n')
    ignored_files = [file.split(':')[1].strip() for file in ignored_files if file]
    ignored_files.sort()
    return ', '.join(ignored_files)