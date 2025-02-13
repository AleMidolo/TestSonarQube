import subprocess

def addignored(ignored):
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    ignored_files = result.stdout.strip().split('\n')
    ignored_files = [file.split(':')[1].strip() for file in ignored_files if file]
    ignored_files.sort()
    return ','.join(ignored_files)