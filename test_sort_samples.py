"""This is a test module for testing the Python sort problem samples.
Python has a rich set of primitives for dealing with sorting.  But just to
refresh our memory of sorting algorithms, we will be implementing and testing
some sort implementations which don't rely upon the built in capabilities.
In the real world, we would not reinvent the wheel.  In some cases, we
will use the built in capabilties for testing purposes

"""
import unittest
from sort_samples import *

class SortSampleTest(unittest.TestCase):
    
    def test_insertion_sort(self):
        """ Test the insertion sort algorithm implementation.

        """
        
        working_list=[1,4,8,9,11,15,7,12,13,6]
        num_sorted=6
        next_pos=num_sorted
        expected_num_sorted=num_sorted + 1
        expected_list=[1,4,7,8,9,11,15,12,13,6]
        actual_num_sorted=insert_sort_val(working_list,num_sorted,
                                          working_list[next_pos])

        self.assertEqual(working_list,expected_list)
        self.assertEqual(actual_num_sorted,expected_num_sorted)

    
        
if __name__== "__main__" :
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
