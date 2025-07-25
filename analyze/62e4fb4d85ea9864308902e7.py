import os

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    if not cmd:
        return cmd

    first_arg = cmd[0]
    if os.name == 'nt' and first_arg.startswith('#!'):
        # On Windows, replace the shebang with the appropriate interpreter
        # Assume the first line is a shebang and extract the interpreter path
        with open(first_arg, 'r') as f:
            first_line = f.readline().strip()
            if first_line.startswith('#!'):
                interpreter = first_line[2:].strip()
                # Split the interpreter path into parts
                interpreter_parts = interpreter.split()
                # The first part is the interpreter path
                interpreter_path = interpreter_parts[0]
                # The rest are arguments to the interpreter
                interpreter_args = interpreter_parts[1:]
                # Replace the shebang with the interpreter and its arguments
                cmd = (interpreter_path,) + tuple(interpreter_args) + cmd[1:]

    return cmd