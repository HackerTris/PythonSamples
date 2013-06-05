"""This is a test module for testing the Python sort problem samples.
Python has a rich set of primitives for dealing with sorting.  But just to
refresh our memory of sorting algorithms, we will be implementing and testing
some sort implementations which don't rely upon the built in capabilities.
In the real world, we would not reinvent the wheel.  In some cases, we
will use the built in capabilties for testing purposes

"""
import unittest
from binary_tree import *

class BinaryTreeTest(unittest.TestCase):
    
    def test_insert_root(self):
        """ Test the insertion sort algorithm implementation.

        """
        
        tree = CBOrdTree()
        root = tree.insert(None, 'A')
        r2=tree.insert(root,'Z')
        r3=tree.insert(root,'F')
        tree.printTree(root)
        
if __name__== "__main__" :
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
