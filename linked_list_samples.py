""" This class implements a basic, singlely linked list.  At this point
in time, the list is NOT sorted.

    The module consists of two classes, the linked list node, and the list
    itself.

    IMPORTANT NOTE:  The need to actually use linked lists in Python
    seems minimal.  But this is a good exercise in basic computer
    science algorthims.

"""

class LinkedListNode():

    def __init__(self,data):
        """ Initialize a node.  The node knows who is points to, which
        is the nextNode.

        """

        self.data = data
        self.next = None




class LinkedList():

    def __init__(self,node=None):
        """ Create the linked list with an initial node, if it is given.
        If not given, then size of the list is one.  If a node is given,
        the size is one and the node is insterted at the beginning of the list.
        It is also the end of the list, since it is the first node.

        """

        if node is not None:
            self.size = 1
            self.first_node = node
            self.last_node = node
            node.next = None

        else:
            self.size = 0
            self.first_node = None
            self.last_node = None

    def pretty_print(self):
        """ Pretty print the list.  Used for testing purposes

        """

        #start with the first node, and go done the list until you reach
        # the last node

        if self.size == 0:
            print("The linked list is empty")
            return
        elif self.size == 1:
            print "The data is: ", self.first_node.data
            return
        node = self.first_node
        while node is not None:
            print "The data is: ",node.data
            node = node.next
        
    def add_node(self,new_node):
        """ Add a new node.  Could do this with data and not the node...

        """

        new_node.next=None
        if self.last_node is None:
            self.last_node = new_node
            self.first_node = new_node
        else:
            self.last_node.next = new_node
            self.last_node = new_node
        self.size+=1

    
    def remove_node(self, del_node):
        """ Remove first node with the data contained in del_node.

        Returns number of nodes removed.  There may be more than
        one with the same data, but we are only going to remove the
        first one.  This makes it a bit more flexible...
        
        """

        
        number_removed = 0
        
        # if our list is empty, we have nothing to return
        
        if self.size == 0:
            return number_removed
        
        node = self.first_node
        prev_node = None
        while node is not None:
            if node.data == del_node.data:
                number_removed += 1

                # case 1- deleting the head

                if node == self.first_node:

                    self.first_node = node.next
                    node.next = None
                    
                    break
        
                # case 2 - deleting the end
                if node == self.last_node:
                    node.next = None
                    if prev_node is not None:
                        self.last_node=prev_node
                        self.last_node.next = None
                    else:
                        self.last_node = None
                    break

                # case 3- deleting in the middle
                
                prev_node.next = node.next
                node.next = None
                break
                
            else:
                # adjust the pointers

                prev_node = node
                node = node.next
 
        
        self.size = self.size - number_removed
        return number_removed
    
    def contains_node(self,test_node):
        """ Determine if there is at least one instance of a
        a node with the given data.  The next pointer in the node
        is irrelevant.  Note that we could have designed the interface
        to accept data and not a node... but it is nice to have
        consistency, one way or the other...

        Returns the first position where the node was found; else,
        returns -1.  Positions start at 0

        """

    
        print
        if self.size == 0:
            return -1

        node =  self.first_node

        pos = 0
        found = False
        while node is not None:
            if node.data == test_node.data:
                found = True
                break
            node = node.next
            pos += 1

        if not found:
            pos = -1

        return pos
