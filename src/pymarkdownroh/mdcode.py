"""Create markdown span of code."""

import re

_CODESPANINDICATOR = "`"

def create_code_span(string: str, start: int = 0, end: int = 1000, word: str = None) -> str:
    """Create a code span in markdown.
    
    A codespan is defined as \`code\`.

    Example:

    \`printf()\`-> `prinf()`
    """

    if start == 0 and end == 1000 and word != None:

        match = re.search(word, string)
        
        return string[:match.span()[0]] + "`" + string[match.span()[0]:match.span()[0] + len(word)] + "`" + string[match.span()[0] + len(word):]

    elif word == None or word not in string:

        return string[:start] + "`" + string[start:end] + "`" + string[end:]

    return "`" + string + "`"
