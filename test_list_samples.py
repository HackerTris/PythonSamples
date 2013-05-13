"""This is a test module for testing the Python array samples module.

"""
import unittest
from list_samples import *

class ListSampleTest(unittest.TestCase):
    
    def test_swap_min_max(self):
        """ Test min max swap of list, with integers

        """
        
        test_list =[-30,99,8,-30,6,99,65]
        print("The min value is: ",min(test_list))
        expected_list=[99,-30,8,99,6,-30,65]
        actual_list=list_swap_min_max(test_list)
        self.assertEqual(expected_list,actual_list,"Lists did not match")

    def test_unique_chars(self):
        """ Test algorithm for a string that has all unique chars
        """
        test_string1="I have several repeated chars."
        test_string2="I am uniqe. "

        # requirements:  all unique characters.  Case sensitive! so I <> i.
        # Blanks and white space are not counted!

        self.assertEqual(unique_chars(test_string1),False)
        self.assertEqual(unique_chars(test_string2),True)
        self.assertEqual(unique_chars("aa"),False)

    def test_reverse_string(self):
        
        test_string="Reverse Me"
        expected_string="eM esreveR"
        self.assertEqual(reverse_string(test_string),expected_string)
        
        
if __name__== "__main__" :
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
