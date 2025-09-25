"""Formatting operations emphasizing strings."""

# Default character used when converting emphasizing string.
_EMPHASIZEPREF = "*"

def write_italics(string: str):
    """Convert provided string to italic string."""

    return _EMPHASIZEPREF + string + _EMPHASIZEPREF

def write_bold(string: str):
    """Convert provided string to bold string."""

    return _EMPHASIZEPREF + _EMPHASIZEPREF + string + _EMPHASIZEPREF + _EMPHASIZEPREF