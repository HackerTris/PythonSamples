"""  This module will test stack and queue samples
    In real life, there may not be a reason to implement these by scratch, as
    Python has many good facilities for such, using lists.

    Python lists make a natural stack because the pop method  (with no args) returns the "last"
    item in the list. The list append method allows you to add items to the list to
    simulate stack semantics

"""

import unittest
from stack_queue_samples import *

class LinkedListSampleTest(unittest.TestCase):

    def test_stack_node (self):
        """ Test only the node creation.  The node is a very simple object
        at this point in time.

        """
        node= StackNode('Storm')
        self.assertEqual(node.data,'Storm')
        self.assertIsNone(node.prev)



    def test_stack_1(self):
        
        """ Create a stack with one node.

        """
        
        node=StackNode('Storm')
        stack=Stack(node)
        self.assertEqual(stack.size,1)
        last=stack.pop()
        self.assertEqual(last.data,node.data)
        self.assertEqual(stack.size,0)
        
              
    def test_stack_push_1(self):
        """ Push node onto sack of size 1

        """
        
        node1=StackNode('Storm')
        stack=Stack(node1)
        node2=StackNode('Janie')
        stack.push(node2)
        self.assertEqual(stack.size,2)
 
        
    def test_stack_pop_1(self):
        """ Pop a node from the stack of size 1

        """
        
        node=StackNode('Storm')
        stack=Stack(node)
        pop_node=stack.pop()
        print(pop_node)
        self.assertEqual(pop_node.data,node.data)
        print("Stack size is: ",stack.size)
        self.assertEqual(stack.size,0)
    

    def test_stack_pop_2(self):
        
        """ Pop a node from the stack size of 2

        """
        
        storm_node=StackNode('Storm')
        stack=Stack(storm_node)
        janie_node=StackNode('Janie')
        stack.push(janie_node)
        pop_node=stack.pop()
        self.assertEqual(pop_node.data,janie_node.data)
        self.assertEqual(stack.size,1)
  

    def test_stack_pop_empty(self):
        """ Try to pop from an empty stack.  Should
        return None

        """
        
        node=StackNode('Storm')
        stack=Stack(node)
        pop_node=stack.pop()
        pop_node_2=stack.pop()

        self.assertIsNone(pop_node_2)
        self.assertEqual(stack.size,0)
        
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit when tests failed
            raise
