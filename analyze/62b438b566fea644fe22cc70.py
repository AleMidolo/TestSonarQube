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
        COMPREPLY=( $(compgen -W '--help --version --verbosity --config --list --init --create --prune --check --extract --info --borg-info --override --dry-run --stats --json --lock-wait --progress --umask --syslog --log-file --log-level --log-json --log-format --log-filter --log-filter-regex --log-filter-invert --log-filter-case --log-filter-level --log-filter-message --log-filter-file --log-filter-line --log-filter-function --log-filter-module --log-filter-path --log-filter-timestamp --log-filter-level-ge --log-filter-level-le --log-filter-level-eq --log-filter-level-ne --log-filter-level-gt --log-filter-level-lt --log-filter-level-ge --log-filter-level-le --log-filter-level-eq --log-filter-level-ne --log-filter-level-gt --log-filter-level-lt' -- ${cur}) )
    else
        COMPREPLY=( $(compgen -W '$(borgmatic --list)' -- ${cur}) )
    fi
}

complete -F _borgmatic_completion borgmatic
"""