import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages

def validate_key(key):
    # Example regex for key validation
    return isinstance(key, str) and re.match(r'^[a-zA-Z0-9_]+$', key)

def validate_value(value):
    # Example regex for value validation
    return isinstance(value, str) and re.match(r'^[a-zA-Z0-9_ ]+$', value)

def _validate_labels(labels):
    """
    检查给定标签中的键和值是否通过 `validate_key()` 和 `validate_value()` 验证。
    检查给定标签中的键和值是否符合其对应的正则表达式。

    参数:
      labels (dict): 需要验证的不同标签。

    异常:
      ValidationError: 如果任何键或值不符合其对应的正则表达式，将抛出此异常。异常消息包含一个错误列表，列出标签中发生的所有错误。列表中的每个元素是一个包含单个键值对的字典：
        - key: 发生错误的标签键或标签值（字符串形式）。
        - value: 错误消息。

        ..示例代码:: python
              # Example:
              labels = {
                  "key1": "valid",
                  "key2": ["invalid"],
                  "$$": "invalid",
                  True: True,
              }
              try:
                  _validate_labels(labels)
              except ValidationError as err:
                  assert err.messages == [
                      {"['invalid']": 'expected string or bytes-like object'},
                      {'$$': "Label key '$$' does not match the regex [...]"},
                      {'True': 'expected string or bytes-like object'},
                      {'True': 'expected string or bytes-like object'},
                  ]
    """
    errors = []
    
    for key, value in labels.items():
        if not validate_key(key):
            errors.append({str(key): f"Label key '{key}' does not match the regex [...]"})
        
        if not validate_value(value):
            errors.append({str(value): 'expected string or bytes-like object'})
    
    if errors:
        raise ValidationError(errors)