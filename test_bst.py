# run with python -m unittest test_bst
import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_instantiation(self):
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Counld not instantiate BinarySearchTree") 

    def test_value(self):
         fake_value = "FAKE"
         bst = BinarySearchTree(fake_value)
         self.assertEqual(bst.value, fake_value)


if __name__ == '__main__':
    unittest.main()
            