"""Create markdown tables with optional column alignment support.

This module provides a very small helper for generating Markdown tables from
plain Python data.  It is intentionally lightweight and does not attempt to
be a full Markdown parser or renderer.

The new ``create_table`` function supports specifying an alignment per
column and will also automatically pad cells so that the returned string is
neatly formatted when viewed in a plain text editor.  The alignment row that
is output uses the usual ``:--``/``--:``/``:--:`` syntax that Markdown
renderers understand.
"""

from __future__ import annotations


def create_table(headers: list, values: list[list],alignments: list[str] | None = None,
) -> str:
    """Return a Markdown table as a string.

    Parameters
    ----------
    headers
        Sequence of column header strings.
    values
        List of rows; each row itself is a sequence with the same length as
        ``headers``.
    alignments
        Optional list of alignment specifiers for each column.  Supported
        values are ``"left"``, ``"center"`` and ``"right"``.  If omitted,
        every column is treated as left aligned.

    Raises
    ------
    ValueError
        If the length of ``alignments`` does not match ``headers`` or if any
        row has a mismatched length.
    """

    # normalize/validate arguments
    if alignments is None:
        alignments = ["left"] * len(headers)

    if len(alignments) != len(headers):
        raise ValueError("alignments must have the same length as headers")

    for a in alignments:
        if a not in ("left", "center", "right"):
            raise ValueError(f"invalid alignment '{a}'")

    table: list[list[str]] = [list(map(str, headers))]
    for row in values:
        if len(row) != len(headers):
            raise ValueError("each row in values must match headers length")
        table.append(list(map(str, row)))

    cols = len(headers)
    widths = [0] * cols
    for r in table:
        for idx, cell in enumerate(r):
            widths[idx] = max(widths[idx], len(cell))

    def _pad(text: str, width: int, alignment: str) -> str:
        if alignment == "left":
            return text.ljust(width)
        elif alignment == "right":
            return text.rjust(width)
        elif alignment == "center":
            return text.center(width)
        return text

    def _sep_marker(width: int, alignment: str) -> str:
        dashes = "-" * max(width, 3)
        if alignment == "left":
            return ":" + dashes[1:]
        elif alignment == "right":
            return dashes[:-1] + ":"
        elif alignment == "center":
            if len(dashes) < 2:
                dashes = "---"
            return ":" + dashes[1:-1] + ":"
        return dashes

    lines: list[str] = []

    # header
    header_cells = [" " + _pad(table[0][i], widths[i], alignments[i]) + " " for i in range(cols)]
    lines.append("|" + "|".join(header_cells) + "|")

    # alignment row
    sep_cells = [" " + _sep_marker(widths[i], alignments[i]) + " " for i in range(cols)]
    lines.append("|" + "|".join(sep_cells) + "|")

    # data rows
    for row in table[1:]:
        cells = [" " + _pad(row[i], widths[i], alignments[i]) + " " for i in range(cols)]
        lines.append("|" + "|".join(cells) + "|")

    return "\n".join(lines)
