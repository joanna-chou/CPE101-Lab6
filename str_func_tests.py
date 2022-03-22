# Lab 6
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07

import unittest
from str_funcs import *

class TestCases(unittest.TestCase):
    def test_vowel_extractor(self):
        self.assertEqual(vowel_extractor("This is a string"),"iiai")
        self.assertEqual(vowel_extractor("Another Piglin?"),"Aoeii")
        self.assertEqual(vowel_extractor("cItiZenShIp"),"IieI")
    
    def test_str_captalize(self):
        self.assertEqual(str_captalize("please capitalize this"), "Please Capitalize This")
        self.assertEqual(str_captalize("AAAAA SCREAming scream"), "AAAAA SCREAming Scream")
        self.assertEqual(str_captalize("what am I doing"), "What Am I Doing")

    def test_str_rotate(self):
        self.assertEqual(str_rotate("a A"), "n N")
        self.assertEqual(str_rotate("nN"), "aA")
        self.assertEqual(str_rotate("Guvf Jvyy Znxr Ab Frafr"), "This Will Make No Sense")
    
    def test_make_substring(self):
        self.assertEqual(make_substring("string", 1,4,1), "tri")
        self.assertEqual(make_substring("b e a ve r", 3, 10,2), "  er")
        self.assertEqual(make_substring("ppeepppaa  dpeiege", 0,17,2), "peppa pig")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("tattarrattat"), True)
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertEqual(is_palindrome("palindrome"), False)
    
    def test_count_characters(self):
        self.assertEqual(count_characters("count characeters", "c"), 3)
        self.assertEqual(count_characters("aaaaaaaaAAAAAaaaasCREAM", "A"), 6)
        self.assertEqual(count_characters("1e2qwrdfadweqe1`2312", "z"), -1)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

