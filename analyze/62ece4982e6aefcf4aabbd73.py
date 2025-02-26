import re
import platform as sys_platform

def split(s, platform='this'):
    """
    在给定的平台下拆分输入字符串，返回拆分结果。  
      如果 `platform` 等于 `'this'`，则自动检测当前平台。  
      如果 `platform` 等于 `1`，使用 POSIX 风格。  
      如果 `platform` 等于 `0`，使用 Windows/CMD 风格。  
      参数：
        s：输入的字符串。  
        platform：  
          `'this'`：根据当前平台自动检测；`1`：使用 POSIX 风格；`0`：使用 Windows/CMD 风格。  
      返回值：
        一个拆分后的字符串列表。
    这是一个用于多平台的 `shlex.split()` 变体，用于命令行字符串的拆分。  
    适用于 `subprocess` 模块，用于 `argv` 参数注入等场景。  
    该方法使用快速的正则表达式（REGEX）实现。

    platform：
      `'this'`：根据当前平台自动检测；  
      `1`：POSIX 风格；  
      `0`：Windows/CMD 风格；  
      （其他值保留）。  
    """
    if platform == 'this':
        platform = 1 if sys_platform.system() != 'Windows' else 0

    if platform == 1:  # POSIX style
        return re.findall(r'(?:"([^"]*)"|\'([^\']*)|(\S+))', s)
    elif platform == 0:  # Windows/CMD style
        return re.findall(r'(?:"([^"]*)"|\'([^\']*)|(\S+)|(\s+)', s)
    else:
        return []