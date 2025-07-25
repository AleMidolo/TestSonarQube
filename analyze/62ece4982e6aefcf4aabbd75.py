def addignored(ignored):
    import subprocess
    
    # Run git ls-files command to get all files
    git_files = subprocess.check_output(['git', 'ls-files', '--others', '--ignored', '--exclude-standard']).decode('utf-8')
    
    # Split output into list and remove empty strings
    files_list = [x for x in git_files.split('\n') if x]
    
    # Sort the list alphabetically
    files_list.sort()
    
    # Join list elements with commas
    ignored_files = ','.join(files_list)
    
    return ignored_files