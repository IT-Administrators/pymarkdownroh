"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir

from src.pymarkdownroh import *

importdir()

TESTS = {
    # Emphasizing tests whole string.
    "EMPHASIZING":["Test"],
    "BOLD_RESULTS":["**Test**"],
    "ITALIC_RESULTS":["*Test*"],
    "BOLDITALIC_RESULTS":["***Test***"],
    # Emphasizing tests substring.
    "EMPHASIZING_SUB": ["Python is great."],
    "BOLD_SUB_RESULTS": ["**Python** is great."],
    "ITALIC_SUB_RESULTS": ["*Python* is great."],
    "BOLDITALIC_SUB_RESULTS": ["***Python*** is great."],

    # Headline tests.
    "HEADLINES":["Title", "Lvl2 Headline", "Lvl3 Headline", "Lvl4 Headline", "Lvl5 Headline", "Lvl6 Headline"],
    "HEADLINE_RESULTS":["# Title", "## Lvl2 Headline", "### Lvl3 Headline", "#### Lvl4 Headline", "##### Lvl5 Headline", "###### Lvl6 Headline"]
}

EXAMPLEFILES = {
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
            self.assertEqual(write_bold(TESTS["EMPHASIZING"][i]),TESTS["BOLD_RESULTS"][i])

    def test_italic_emphasizing(self):
        for i in range(len(TESTS["EMPHASIZING"])):
            self.assertEqual(write_italics(TESTS["EMPHASIZING"][i]),TESTS["ITALIC_RESULTS"][i])

    def test_bold_italic_emphasizing(self):
        for i in range(len(TESTS["EMPHASIZING"])):
            self.assertEqual(write_bold_italic(TESTS["EMPHASIZING"][i]),TESTS["BOLDITALIC_RESULTS"][i])

    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            self.assertEqual(write_bold(TESTS["EMPHASIZING_SUB"][i], startbold=0, endbold=6), TESTS["BOLD_SUB_RESULTS"][i])
    
    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            self.assertEqual(write_italics(TESTS["EMPHASIZING_SUB"][i], startitalic=0, enditalic=6), TESTS["ITALIC_SUB_RESULTS"][i])

    def test_bold_emphasizing_substring(self):
        for i in range(len(TESTS["EMPHASIZING_SUB"])):
            self.assertEqual(write_bold_italic(TESTS["EMPHASIZING_SUB"][i], startboldital=0, endboldital=6), TESTS["BOLDITALIC_SUB_RESULTS"][i])

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
    

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()