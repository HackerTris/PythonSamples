"""  This module will test linked list objects and classes.

"""

import unittest
from linked_list_samples import *

class LinkedListSampleTest(unittest.TestCase):

    def test_linked_list_node (self):
        """ Test only the node creation.  The node is a very simple object
        at this point in time.

        """
        node= LinkedListNode('Storm')
        self.assertEqual(node.data,'Storm')
        self.assertIsNone(node.next)


    def test_linked_list_zero_node(self):
        """ Create a linked list with no nodes.

        """
        linked_list=LinkedList()
        self.assertEqual(linked_list.size,0)
        self.assertIsNone(linked_list.first_node)
        self.assertIsNone(linked_list.last_node)

    def test_linked_list_one_node(self):
        """ Create a linked list with one node.

        """
        
        node=LinkedListNode('Storm')
        linked_list=LinkedList(node)
        self.assertEqual(linked_list.first_node.data,'Storm')
        self.assertEqual(linked_list.last_node.data,'Storm')
        self.assertEqual(linked_list.size,1)
        
        
    def test_linked_list_add_to_0(self):
        """ Add a node to a linked list with 0 nodes

        """
        
        node=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node)
        self.assertEqual(linked_list.first_node.data,'Storm')
        self.assertEqual(linked_list.last_node.data,'Storm')
        self.assertEqual(linked_list.size,1)
        

    def test_linked_list_add_to_1(self):
        """ Add a node to a list containing one other node

        """
        node=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node)
        node=LinkedListNode('Janie')
        linked_list.add_node(node)
        self.assertEqual(linked_list.first_node.data,'Storm')
        self.assertEqual(linked_list.last_node.data,'Janie')
        self.assertEqual(linked_list.size,2)
 
        

    def test_linked_list_contains_1_node(self):
        """ Test if the list contains a node with the data.  We
        don't care about the next pointer.

        We could benefit from text fixture setup here.... 

        """

        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        node2=LinkedListNode('Janie')
        linked_list.add_node(node2)
        self.assertEqual(linked_list.contains_node(node1),0)
        self.assertEqual(linked_list.contains_node(node2),1)
        
    def test_linked_list_contains_multi_nodes(self):
        """ Test if the list contains a certain data set, when
        there are multiple such nodes.  We don't care about the next
        pointers.

        """
        pass

    def test_linked_list_not_contains_node(self):
        """ Test if the list does not contain the indicated node

        """
        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        node2=LinkedListNode('Janie')
        linked_list.add_node(node2)
        node3=LinkedListNode('Seamus')
        self.assertEqual(linked_list.contains_node(node3),-1)

    def test_linked_list_remove_1_middle(self):

        """ Remove a node where there is one instance of the node
        We will remove the middle node

        """
    
        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        node2=LinkedListNode('Janie')
        linked_list.add_node(node2)
        node3=LinkedListNode('Seamus')
        linked_list.add_node(node3)

        self.assertEqual(linked_list.contains_node(node2),1)
        self.assertEqual(linked_list.remove_node(node2),1)
        self.assertEqual(linked_list.contains_node(node2),-1)
        

    def test_linked_list_remove_1_multiple (self):

        """ Remove a node where there are multiple instances of the node
        We will remove the middle node

        """
    
        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        node2=LinkedListNode('Janie')
        linked_list.add_node(node2)
        node3=LinkedListNode('Janie')
        linked_list.add_node(node3)
        node4=LinkedListNode('Seamus')
        linked_list.add_node(node4)

        
        self.assertEqual(linked_list.contains_node(node2),1)
        self.assertEqual(linked_list.remove_node(node2),1)
        self.assertEqual(linked_list.contains_node(node3),1)
        
        
    def test_linked_list_remove_1_end(self):
        """ Test case where we remove one node at the tail

        """

        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        node2=LinkedListNode('Janie')
        linked_list.add_node(node2)
        self.assertEqual(linked_list.remove_node(node2),1)
        self.assertEqual(linked_list.size,1)
 
        
    def test_linked_list_remove_1_head(self):
        """ Test removing the head and it is the only node
        """
        node1=LinkedListNode('Storm')
        linked_list=LinkedList()
        linked_list.add_node(node1)
        self.assertEqual(linked_list.remove_node(node1),1)
        self.assertEqual(linked_list.size,0)
        
        
    def test_duplicate_removal(self):
        """Remove duplicate chars from the following string:
         FOLLOW.

         Normally, we would put this in a unit test case.  But this is working
         through the examples in the book, and we are sort of testing
         the utility of the module...
         """

        #first, create a linked list with each letter of "Follow" a node

        w="FOLLLOW"
        linked_list=LinkedList()
        d={}
        for l in w:
            node = LinkedListNode(l)
            if l in d:
                d[l] += 1
            else:
                d[l]=1
            linked_list.add_node(node)
        linked_list.pretty_print()

        # now we will remove duplicates
        for l in d.keys():
            for dupes in range(1,d[l]):
                linked_list.remove_node(LinkedListNode(l))

        # I should write some methods in the linked list class
        # so this can be tested properly....
        
        link_list.pretty_print()
    
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit when tests failed
            raise
