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

    # Headline tests.
    "HEADLINES":["Title", "Lvl2 Headline", "Lvl3 Headline", "Lvl4 Headline", "Lvl5 Headline", "Lvl6 Headline"],
    "HEADLINE_RESULTS":["# Title", "## Lvl2 Headline", "### Lvl3 Headline", "#### Lvl4 Headline", "##### Lvl5 Headline", "###### Lvl6 Headline"]
}

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

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()