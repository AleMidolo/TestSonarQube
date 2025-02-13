from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    base = len(alphabet)
    result = []

    if number == 0:
        result.append(alphabet[0])

    while number > 0:
        result.append(alphabet[number % base])
        number //= base

    result.reverse()
    result_str = ''.join(result)

    if padding is not None:
        result_str = result_str.zfill(padding)

    return result_str