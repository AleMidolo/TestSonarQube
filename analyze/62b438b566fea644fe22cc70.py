def bash_completion():
    """
    बॉर्गमैटिक कमांड के लिए बाश कम्प्लीशन स्क्रिप्ट लौटाएं।  
    यह स्क्रिप्ट बॉर्गमैटिक के कमांड-लाइन आर्ग्युमेंट पार्सर्स का निरीक्षण करके उत्पन्न की जाती है।
    """
    return """
_borgmatic_completion() {
    local cur prev words cword
    _init_completion || return

    if [[ ${cur} == -* ]]; then
        COMPREPLY=($(compgen -W '-h --help -v --version -c --config -d --debug -q --quiet -n --dry-run -e --encryption -r --repository -a --archive -p --passphrase -l --list -i --info -x --extract -m --mount -b --borg -s --stats -t --test -u --upload -y --yes' -- ${cur}))
    else
        COMPREPLY=($(compgen -W 'init create prune check list info extract mount borg stats test upload' -- ${cur}))
    fi
}

complete -F _borgmatic_completion borgmatic
"""