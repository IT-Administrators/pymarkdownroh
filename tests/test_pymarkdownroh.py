"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir

from src.pymarkdownroh import *

importdir()

TESTS = {
    # Blockquoting the provided string.
    "BLOCKSTRING": ["This is a blockquote.","""This is a multiline
string."""],
    "BLOCKQUOTE_RESULT": ["> This is a blockquote.","""> This is a multiline
> string."""],

    # Emphasizing tests whole string.
    "EMPHASIZING": ["Test"],
    "BOLD_RESULTS": ["**Test**"],
    "ITALIC_RESULTS": ["*Test*"],
    "BOLDITALIC_RESULTS": ["***Test***"],
    # Emphasizing tests substring.
    "EMPHASIZING_SUB": ["Python is great."],
    # Tuple of (startposition, endposition, result).
    "BOLD_SUB_RESULTS": [(0, 6, "**Python** is great.")],
    "ITALIC_SUB_RESULTS": [(0, 6, "*Python* is great.")],
    "BOLDITALIC_SUB_RESULTS": [(0, 6, "***Python*** is great.")],

    "HORIZONTALRULE_RESULT": ["* * *"],

    # Headline tests.
    "HEADLINES": ["Title", "Lvl2 Headline", "Lvl3 Headline", "Lvl4 Headline", "Lvl5 Headline", "Lvl6 Headline"],
    "HEADLINE_RESULTS": ["# Title", "## Lvl2 Headline", "### Lvl3 Headline", "#### Lvl4 Headline", "##### Lvl5 Headline", "###### Lvl6 Headline"],

    # Link tests.
    # list[tuple(linktext, url, linktitle)]
    "INLINE_LINKS": [("An Example","www.example.com","Example Title"),
                     ("An Example","www.example.com", "")],
    "INLINE_LINKS_RESULTS": ["[An Example](www.example.com \"Example Title\")",
                             "[An Example](www.example.com)"],
    "AUTOMATED_LINKS": ["http://www.example.com","example@example.com"],
    "AUTOMATED_LINKS_RESULTS": ["<http://www.example.com>", "<example@example.com>"],
    # list[tuple(linktext, linkname, url, linktitle)]
    "REFERENCE_LINKS": [("Link Text","Link Name","www.example.com","Link Title"),
                        ("Link Text","Link Name","www.example.com","")],
    "REFERENCE_LINKS_RESULTS": ["[Link Text][Link Name]\n\n[Link Name]: www.example.com (Link Title)", "[Link Text][Link Name]\n\n[Link Name]: www.example.com"]}

EXAMPLEFILES = {
    "BLOCKQUOTES": "./examples/BLOCKQUOTES.md",
    "EMPHASIZING": "./examples/EMPHASIZE.md",
    "HEADLINES": "./examples/HEADLINES.md",
    "TABLES": "./examples/TABLES.md"
}

class TestPymarkdownroh_Emphasizing(unittest.TestCase):
    """Test emphasizing of pymarkdownroh module.."""

    def setUp(self):
        self.tests = TESTS

    def test_bold_emphasizing(self):
        for i in range(len(TESTS["EMPHASIZING"])):
            testobj = MDFormat(string=TESTS["EMPHASIZING"][i])
            self.assertEqual(testobj.write_bold(), TESTS["BOLD_RESULTS"][i])

    def test_italic_emphasizing(self):
        for i in range(len(TESTS["EMPHASIZING"])):
            testobj = MDFormat(string=TESTS["EMPHASIZING"][i])
            self.assertEqual(testobj.write_italic(), TESTS["ITALIC_RESULTS"][i])

    def test_bold_italic_emphasizing(self):
        for i in range(len(TESTS["EMPHASIZING"])):
            testobj = MDFormat(string=TESTS["EMPHASIZING"][i])
            self.assertEqual(testobj.write_bold_italic(), TESTS["BOLDITALIC_RESULTS"][i])

    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            testobj = MDFormat(TESTS["EMPHASIZING_SUB"][i], TESTS["BOLD_SUB_RESULTS"][i][0], TESTS["BOLD_SUB_RESULTS"][i][1])
            self.assertEqual(testobj.write_bold(), TESTS["BOLD_SUB_RESULTS"][i][2])
    
    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            testobj = MDFormat(TESTS["EMPHASIZING_SUB"][i], TESTS["ITALIC_SUB_RESULTS"][i][0], TESTS["ITALIC_SUB_RESULTS"][i][1])
            self.assertEqual(testobj.write_italic(), TESTS["ITALIC_SUB_RESULTS"][i][2])

    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            testobj = MDFormat(TESTS["EMPHASIZING_SUB"][i], TESTS["BOLDITALIC_SUB_RESULTS"][i][0], TESTS["BOLDITALIC_SUB_RESULTS"][i][1])
            self.assertEqual(testobj.write_bold_italic(), TESTS["BOLDITALIC_SUB_RESULTS"][i][2])

    def test_horizontal_rule(self):
        for i in range(len(TESTS["HORIZONTALRULE_RESULT"])):
            self.assertEqual(MDFormat.create_horizontal_rule(), TESTS["HORIZONTALRULE_RESULT"][i])

class TestPymarkdownroh_Headlines(unittest.TestCase):
    """Test headline and title creation of pymarkdownroh module."""

    def setUp(self):
        self.tests = TESTS

    def test_headline(self):
        for i in range(len(TESTS["HEADLINES"])):
            # Create with i +1 because the lsit starts counting by zero but a headline must have one #.
            self.assertEqual(create_headline(i +1, TESTS["HEADLINES"][i]), TESTS["HEADLINE_RESULTS"][i])

            with open(EXAMPLEFILES["HEADLINES"], "w") as f:
                for i in range(len(TESTS["HEADLINES"])):
                    f.write(create_headline(i +1, TESTS["HEADLINES"][i]) + "\n")
    
class TestPymarkdownroh_Blockquotes(unittest.TestCase):
    """Test blockquote creation of pymarkdownroh module."""

    def setUp(self):
        self.tests = TESTS

    def test_blockquote(self):
        for i in range(len(TESTS["BLOCKSTRING"])):
            self.assertEqual(create_blockquote(TESTS["BLOCKSTRING"][i]), TESTS["BLOCKQUOTE_RESULT"][i])

class TestPymarkdownroh_Links(unittest.TestCase):
    """Test link creation or pymarkdownroh module."""

    def setUp(self):
        self.tests = TESTS

    def test_inline_link(self):
        for i in range(len(TESTS["INLINE_LINKS"])):
            link = MDLink(linktext= TESTS["INLINE_LINKS"][i][0], url= TESTS["INLINE_LINKS"][i][1], title= TESTS["INLINE_LINKS"][i][2])
            self.assertEqual(link.create_inline_link(), TESTS["INLINE_LINKS_RESULTS"][i])

    def test_automated_link(self):
        for i in range(len(TESTS["AUTOMATED_LINKS"])):
            link = MDLink(url = TESTS["AUTOMATED_LINKS"][i])
            self.assertEqual(link.create_automatic_link(), TESTS["AUTOMATED_LINKS_RESULTS"][i])

    def test_reference_link(self):
        for i in range(len(TESTS["REFERENCE_LINKS"])):

            link = MDLink(linktext=TESTS["REFERENCE_LINKS"][i][0], linkname= TESTS["REFERENCE_LINKS"][i][1], url= TESTS["REFERENCE_LINKS"][i][2], title=TESTS["REFERENCE_LINKS"][i][3])
            self.assertEqual(link.create_reference_link(), TESTS["REFERENCE_LINKS_RESULTS"][i])


if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()