import arrays_and_strings
import unittest

class MyAppUnitTestCase(unittest.TestCase):

    def test_has_unique_chars(self):
        self.assertFalse(arrays_and_strings.has_unique_chars("pineapple"))
        self.assertTrue(arrays_and_strings.has_unique_chars("sequioa"))
        self.assertFalse(arrays_and_strings.has_unique_chars("I can't smile"))

    
    def test_is_permutation(self):
        self.assertFalse(arrays_and_strings.is_permutation("pineapple", "neaplepi"))
        self.assertTrue(arrays_and_strings.is_permutation("sequioa", "aoiequs"))
        self.assertFalse(arrays_and_strings.is_permutation("I can't smile", "I can't smilt"))

    
    def test_make_url(self):
        self.assertEqual(arrays_and_strings.make_url("  my web site "), "my%20web%20site")
        self.assertEqual(arrays_and_strings.make_url("   mywebsite "), "mywebsite") 
        self.assertEqual(arrays_and_strings.make_url(""), "") 


    def test_is_palindrome_perm(self):
        self.assertFalse(arrays_and_strings.is_palindrome_perm("Taco"))
        self.assertTrue(arrays_and_strings.is_palindrome_perm("Taco Coa"))
        self.assertFalse(arrays_and_strings.is_palindrome_perm("Taco Coaa"))


    def test_one_away(self):
        self.assertTrue(arrays_and_strings.one_away("pale","ple"))
        self.assertTrue(arrays_and_strings.one_away("pales","pale"))
        self.assertTrue(arrays_and_strings.one_away("pale","bale"))
        self.assertFalse(arrays_and_strings.one_away("pale","bake"))
        self.assertFalse(arrays_and_strings.one_away("park","parker"))

    def test_compress_string(self):
        self.assertEqual(arrays_and_strings.compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(arrays_and_strings.compress_string("abc"), "abc") 
        self.assertEqual(arrays_and_strings.compress_string("aAAAaaabBBcc"), "a1A3a3b1B2c2") 

    def test_rotate_matrix(self):
        self.assertEqual(arrays_and_strings.rotate_matrix([[1,2],[3,4]]), [[3,1],[4,2]])
        self.assertEqual(arrays_and_strings.rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(arrays_and_strings.rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])


if __name__ == "__main__":
    unittest.main()