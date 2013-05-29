"""  This module will test the "animal shelter app"
    The business rules for this animal shelter are:

    1. Operates on a first in, first out basis.
    2. enqueue:  will enqueue a dog or cat
    3. get_pet:  will retrieve the animal, whether cat or dog, in the shelter
    the longest.
    4. get_dog:  Will retrieve the dog in the shelter the longest
    5. get_cat:  Will retreive the cat who was in the shelter longest

"""

import unittest
from animal_shelter import *

class AnimalShelterTest (unittest.TestCase):

    def test_cat_create(self):
        """ Test creating a cat pet.

        """
        cat=Cat('Muffin')
        print(cat)

    def test_dog_create(self):
        """ Test creating a dog pet.

        """
        pass
    def test_enqueue_dog_0(self):
        """ This method will test enqueuing a dog in the shelter when there
        are no other animals

        """
        pass
    def test_enqueue_cat_1(self):
        """ Enqueue a cat with one other animal in the shelter

        """
        pass
    def test_enqueue_dog_2(self):
        """ Enqueue a dog when there are two animals in the shelter

        """
        pass

    def test_get_pet_0(self):
        """ Test trying to get a pet from the shelter when it is empty

        """
        pass
    def test_get_dog_0(self):
        """ Test trying to get a dog when there are only cats in the shelter

        """
        pass
    def test_get_dog(self):
        """ Test getting the dog who has been in the shelter the longest.

        """
        pass
    def test_get_pet(self):
        """ Test getting the pet who has been in the shelter the longest

        """

    def test_get_cat(self):
        """ Test getting the cat who has been in the shelter the longests

        """
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit when tests failed
            raise
