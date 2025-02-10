import re, json
import tiktoken

def num_tokens_from_string(string: str) -> int:
    encoding = tiktoken.encoding_for_model("gpt-4o")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def extract_function_signature(code):
    # Regular expression to match the function signature and the docstring
    pattern = r"def.*?:\n"
    match = re.search(pattern, code, re.DOTALL)
    
    if match:
        return match.group(0)
    else:
        pattern = r"def.*?: "
        match = re.search(pattern, code, re.DOTALL)

        if match:
            return match.group(0)
        return None
    
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def getSignaturePython(method_code):
    method_code = method_code.strip()
    lines = [line for line in method_code.split("\n") if not (line.strip().startswith("import") or line.strip().startswith("from"))]

    signature_line = ""
    for line in lines:
        signature_line += line.strip()
        if ":" in line:
            break

    return signature_line