""" This class and animal shelter using a LinkedList and first in, first out
    semantics.

    The business rules for this animal shelter are:

    1. Operates on a first in, first out basis.
    2. enqueue:  will enqueue a dog or cat
    3. get_pet:  will retrieve the animal, whether cat or dog, in the shelter
    the longest.
    4. get_dog:  Will retrieve the dog in the shelter the longest
    5. get_cat:  Will retreive the cat who was in the shelter longest

"""

 

from linked_list_samples import *

class Cat(LinkedListNode):

    def __init__(self,name):
        """ Initialize cat with a name. """
        
        self.name=name
        LinkedListNode.__init__(self,name)

    def __repr__(self):
        """ Create reprcatesentation of this object.

        """
        str="Cat's name: " + self.name
        if self.next is None:
            str = str + "." + " No animals entered shelter after this one. "
        else:
            str=str + "." + " This animal entered the shelter before this one: " + self.prev.data

        return str

class Shelter(LinkedList):

    def __init__(self,animal=None):
        pass
    
