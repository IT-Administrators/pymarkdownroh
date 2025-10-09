"""Formatting operations emphasizing strings."""

# Default character used when converting emphasizing string.
_EMPHASIZEPREF = "*"

_EMPHASIZEKIND = {
    "bold": f"{_EMPHASIZEPREF + _EMPHASIZEPREF}",
    "italic": f"{_EMPHASIZEPREF}",
    "boldItalic": f"{_EMPHASIZEPREF + _EMPHASIZEPREF+ _EMPHASIZEPREF}"
}

def write_bold(string: str):
    """Convert provided string to bold string."""

    return _EMPHASIZEKIND["bold"] + string + _EMPHASIZEKIND["bold"]

def write_italics(string: str):
    """Convert provided string to italic string."""

    return _EMPHASIZEKIND["italic"] + string + _EMPHASIZEKIND["italic"]

def write_bold_italic(string: str):
    """Convert provided string to italic and bold."""

    return _EMPHASIZEKIND["boldItalic"] + string + _EMPHASIZEKIND["boldItalic"]