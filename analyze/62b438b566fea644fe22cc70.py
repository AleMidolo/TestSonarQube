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
        COMPREPLY=($(compgen -W '--help --version --verbosity --config --list --create --prune --check --extract --info --init --upgrade --version' -- ${cur}))
    else
        COMPREPLY=($(compgen -f -- ${cur}))
    fi
}

complete -F _borgmatic_completion borgmatic
"""