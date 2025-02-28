def bash_completion():
    """
    बॉर्गमैटिक कमांड के लिए बाश कम्प्लीशन स्क्रिप्ट लौटाएं।  
    यह स्क्रिप्ट बॉर्गमैटिक के कमांड-लाइन आर्ग्युमेंट पार्सर्स का निरीक्षण करके उत्पन्न की जाती है।
    """
    completion_script = """
_borgmatic_completion() {
    local cur prev words cword
    _init_completion || return

    if [[ ${cur} == -* ]]; then
        COMPREPLY=($(compgen -W '--help --version --verbosity --config --list --create --prune --check --extract --info --init --stats --umask --lock-wait --override --json --dry-run --progress --remote-path --remote-ratelimit --remote-buffer --remote-ssh' -- ${cur}))
    else
        COMPREPLY=($(compgen -f -- ${cur}))
    fi
}

complete -F _borgmatic_completion borgmatic
"""
    return completion_script