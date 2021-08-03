from haskell_test_haskython import incList, decList, sumList, power

import unittest


class TestLargerTestsHaskellTestHaskython(unittest.TestCase):

    def test_incList_haskythonTest(self):
        listToInc = [1,2,3,4,5]
        expected = [2,3,4,5,6]
        il = incList(listToInc)
        self.assertEqual(il, expected)


    def test_decList_haskythonTest(self):
        listToDec = [2,4,6,8,10]
        expected = [1,3,5,7,9]
        dl = decList(listToDec)
        self.assertEqual(dl, expected)

    
    def test_sumList_haskythonTest(self):
        listToSum = [3,6,9,12,15]
        expected = 45
        sl = sumList(listToSum)
        self.assertEqual(sl, expected)


    def test_power_haskythonTest(self):
        powerBase = 2
        powerExponent = 3
        expected = 8
        p = power(powerBase, powerExponent)
        self.assertEqual(p, expected)


if __name__ == '__main__':
    unittest.main()
