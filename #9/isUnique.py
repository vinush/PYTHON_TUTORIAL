# Is unique: implement an algorithm to dertemine if a string has all uniuque character
import unittest


def unique(str):
    # hin: hash table => dict: key-value
    char_set = {}

    for char in str:
        # print(char)
        if char in char_set:
            return False
        char_set[char] = True
    return True


class Test(unittest.TestCase):
    dataT = [("abcs"), ("ewf213"), ("")]
    dataF = [("232sd"), ("hb ddasdasd jav")]

    def test_unique(self):
        # true check
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
        # false
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)


if __name__ == "__main__":
    # str = "31254231dswdq31435"
    # print(unique(str))
    unittest.main()
