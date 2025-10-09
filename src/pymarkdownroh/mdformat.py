"""Formatting operations emphasizing strings."""

# Default character used when converting emphasizing string.
_EMPHASIZEPREF = "*"

_EMPHASIZEKIND = {
    "bold": f"{_EMPHASIZEPREF + _EMPHASIZEPREF}",
    "italic": f"{_EMPHASIZEPREF}",
    "boldItalic": f"{_EMPHASIZEPREF + _EMPHASIZEPREF+ _EMPHASIZEPREF}"
}

def write_bold(string: str, startbold: int = 0, endbold: int = 1000) -> str:
    """Convert provided string to bold string."""

    _verify_range(startbold, endbold)
    return string[:startbold] + _EMPHASIZEKIND["bold"] + string[startbold:endbold] + _EMPHASIZEKIND["bold"] + string[endbold:]

def write_italics(string: str, startitalic:int = 0, enditalic: int = 1000) -> str:
    """Convert provided string to italic string."""

    _verify_range(startitalic, enditalic)
    return string[:startitalic] + _EMPHASIZEKIND["italic"] + string[startitalic:enditalic] + _EMPHASIZEKIND["italic"] + string[enditalic:]


def write_bold_italic(string: str, startboldital: int = 0, endboldital: int = 1000) -> str:
    """Convert provided string to italic and bold."""

    _verify_range(startboldital, endboldital)
    return string[:startboldital] + _EMPHASIZEKIND["boldItalic"] + string[startboldital:endboldital] + _EMPHASIZEKIND["boldItalic"] + string[endboldital:]


def _verify_range(start: int, end: int) -> Exception:
    if end < start:
        raise ValueError(f"End {end} smaller than Start {start}.")
