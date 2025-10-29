"""Create markdown links."""

from typing import Optional

class MDLink:
    """Class for creating different kinds of links."""

    def __init__(self, linktext:str = "An Example", url:str = "www.example.com", title: Optional[str] = "Example", linkname: Optional[int | str] = 1):
        self.linktext = linktext
        self.url = url
        self.title = title
        self.linkname = linkname

    def create_inline_link(self) -> str:
        """
        Create inline link.
        
        An inline link is defined as:

        \[linktext](url)
        """
        # Check if title is set. If so return markdown link with title.
        if not self.title == "" or not self.title == None:
            return "[" + self.linktext + "]" + "(" + self.url + " " + '"' + self.title + '"' + ")"
        
        return "[" + self.linktext + "]" + "(" + self.url + ")"
    
    def create_reference_link(self) -> str:
        """
        Create reference link.

        \[linktext][linkname]
        
        \[linkname]: [url]
        """
        # Check if title is set. If so return markdown link with title.
        if not self.title == "" or not self.title == None:
            return _create_reference_text_name(self.linktext, self.linkname) + "\n" + "\n" + _create_reference_name_url(self.linkname, self.url, self.title)

        return _create_reference_text_name(self.linktext, self.linkname) + "\n" + "\n" + _create_reference_name_url(self.linkname, self.url)

def _create_reference_text_name(linktext:str, linkname: str) -> str:
    """
    Create a reference to the given link.
    
    A reference looks like this:

    \[linktext][linkname]    
    """

    return "[" + linktext + "]" + "[" + str(linkname) + "]"

def _create_reference_name_url(linkname:str, url: str, title:str = None) -> str:
    """
    Create the link to the given reference.
    
    \[linkname]: [url]
    """

    # Check if title is set. If so return markdown link with title.
    if not title == "" or not title == None:
        return "[" + str(linkname) + "]" + ":" + " " + url + " " + "(" + title + ")"

    return "[" + str(linkname) + "]" + ":" + " " + url