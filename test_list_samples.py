"""This is a test module for testing the Python array samples module.

"""
import unittest
from list_samples import *

class ListSampleTest(unittest.TestCase):
    
    def test_swap_min_max(self):
        """ Test min max swap of list, with integers

        """
        
        test_list =[-30,99,8,-30,6,99,65]
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
        """ Test string reverse operation.  easy to do in python with backward
        skips s[::-1]
        """
        test_string="Reverse Me"
        expected_string="eM esreveR"
        self.assertEqual(reverse_string(test_string),expected_string)

    def test_string_permutation(self):
        """ Test function which determines if one string is a permutation of
        another.
        """
        test_string1="cba"
        test_string2="acb"

        self.assertEqual(permutation_string(test_string1,test_string2),True)

        # now test the reverse

        test_string3="da"
        self.assertEqual(permutation_string(test_string1,test_string3),False)

    def test_matrix_transform(self):
        """ Test function that, given an mxn matrix, if any element is 0, then
        all elements in the row are tranformed to 0 and all elements in the column.

        Examples:  assume the matrix is implemented as a list of lists.

        [[0,1,2], [3,4,5]] represents a 2x3 matrix, where there are two rows
        and three columns.  Since element 0,0 is 0, then all elements in the first row
        are 0 and all elements in the first column are zero.  This would
        lead to a matrix represented as: [[0,0,0], [0,4,5]]
        
        """

        m_test=[[0,1,2],[3,4,5]]
        m_expected=[[0,0,0],[0,4,5]]
        self.assertEqual(matrix_transform(m_test),m_expected)

        #test the case where there are no 0's, so the transformed matrix is the
        #same as the starting matrix

        m_test=[[1,2,3],[4,5,6]]
        self.assertEqual(matrix_transform(m_test),m_test)

        #test case with 0's in different positions in each row

        m_test=[[0,1,2],[3,0,4],[5,6,0]]
        m_expected=[[0,0,0],[0,0,0],[0,0,0]]

        self.assertEqual(matrix_transform(m_test),m_expected)

        m_test=[[0,0,1],[2,3,4],[5,6,7]]
        m_expected=[[0,0,0],[0,0,4],[0,0,7]]
        self.assertEqual(matrix_transform(m_test),m_expected)
        
if __name__== "__main__" :
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
