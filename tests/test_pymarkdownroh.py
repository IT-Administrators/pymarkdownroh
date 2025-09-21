"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir

from src.pymarkdownroh import MarkDown

importdir()

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()