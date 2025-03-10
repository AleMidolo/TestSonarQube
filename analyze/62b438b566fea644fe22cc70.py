def bash_completion():
    """
    Devuelve un script de autocompletado para bash para el comando de borgmatic. Esto se genera mediante la introspección de los analizadores de argumentos de línea de comandos de borgmatic.
    """
    import subprocess
    import sys

    # Obtener la salida de borgmatic --help
    try:
        help_output = subprocess.check_output(["borgmatic", "--help"], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar borgmatic --help: {e.output}", file=sys.stderr)
        return ""

    # Generar el script de autocompletado
    bash_script = """
_borgmatic_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="$(borgmatic --help | grep -oP '^\\s+\\K\\S+' | tr '\\n' ' ')"
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}
complete -F _borgmatic_completion borgmatic
"""
    return bash_script