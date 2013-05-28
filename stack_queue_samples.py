""" This class implements a basic stack.

    The module consists of two classes, the StackNode and the stack
    itself.

    IMPORTANT NOTE:  The need to actually a stack of this nature is
    almost non-existant in the real world, due to the facilities of Python
    lists.

"""

class StackNode():

    def __init__(self,data):
        """ Initialize a node.  The node knows who is points to, which
        is the nextNode.

        """

        self.data = data
        self.prev = None

    def __repr__(self):
        """ Create representation of this object.

        """
        str="Data: " + self.data
        if self.prev is None:
            str = str + "." + " Pointer node is None"
        else:
            str=str + "." + " Pointer node data is: " + self.prev.data

        return str

class Stack():

    def __init__(self,node=None):
        """ Create the stack with an initial node, if it is given.
        If not given, then the stack is empty.  If a node is given,
        the size is one.

        """

        if node is not None:
            self.size = 1
            self.top  = node
            self.bottom = node
            node.prev = None

        else:
            self.size = 0
            self.top = None
            self.bottom = None
 

    def pretty_print(self):
        """ Pretty print the stack.  Used for testing purposes.  This
        will print with the top of the stack fierst.

        """

        #start with the first node, and go done the list until you reach
        # the last node

        if self.size == 0:
            print("The stack is empty")
            return
        elif self.size == 1:
            print "The data is: ", self.top.data
            return
        node = self.top
        while node is not None:
            print "The data is: ",node.data
            node = node.prev
        
    def push(self,node):
        """ Push a node to the top of the stack

        """

        if self.top is None:  # was empty
            self.top = node
            self.bottom = node
            node.prev = None
        else:
            node.prev = self.top
            self.top = node
        
        
        self.size+=1

    
    def pop(self):
        """ Pop the top node off the stack, adjusting accordingly

        """
        if self.size == 0:
            return None
        elif self.size == 1:
            node = self.top
            self.top = None
            self.bottom = None
 
        else:
            node = self.top
            self.top = node.prev
            node.prev = None
            
        self.size = self.size -1
        return node
    
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

        node =  self.top

        pos = 0
        found = False
        while node is not None:
            if node.data == test_node.data:
                found = True
                break
            node = node.prev
            pos += 1

        if not found:
            pos = -1

        return pos
