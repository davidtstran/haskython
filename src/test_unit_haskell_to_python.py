from haskell_to_python import parseFunctionDeclaration, parseChoices, collectFunctionMethod

import unittest


class TestUnitHaskellToPython(unittest.TestCase):

    def test_parseFunctionDeclaration(self):
        declaration = "incList :: [Integer] -> [Integer]"
        pfd = parseFunctionDeclaration(declaration)
        self.assertEqual(pfd, "def incList (integer_list0,):")


    def test_parseChoices_EmptyList(self):
        choice = "incList [] = []"
        expected = "\n\tif integer_list0 == []:\n\t\treturn []"
        pc = parseChoices(choice, 0)
        self.assertEqual(pc, expected)


    def test_parseChoices(self):
        choice = "incList (x:xs) = x+1 : incList xs"
        expected = "\n\telse:\n\t\t"
        expected += "returnList = [integer_list0[0]+1]"
        expected += "\n\t\treturnList.extend(incList(integer_list0[1:]))"
        expected += "\n\t\treturn returnList"
        pc = parseChoices(choice, 0)
        self.assertEqual(pc, expected)


    def test_collectFunctionMethod(self):
        choice = "x * power x (y - 1)"
        params = ["power", "x", "y"]
        expected = "return integer0 * power(integer0, (integer1 - 1))"
        cfm = collectFunctionMethod(choice, params)
        self.assertEqual(cfm, expected)


if __name__ == '__main__':
    unittest.main()
