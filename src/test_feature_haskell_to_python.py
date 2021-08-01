import haskell_to_python

import unittest
import os.path
from os import path

class TestFeatureHaskellToPython(unittest.TestCase):

    def test_createPythonFileFromHaskellFile(self):
        file_name = "haskell_test_empty.hs"
        haskell_to_python.main(file_name)
        self.assertTrue(path.exists(f"{file_name[:-3]}_haskython.py"))


if __name__ == '__main__':
    unittest.main()
