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

    def test_insert_to_root_lesser(self):
        bst = BinarySearchTree(55)
        child = BinarySearchTree(25)
        bst.insert(child)
        self.assertEqual(bst.left, child)

    def test_insert_to_root_greater(self):
        bst = BinarySearchTree(55)
        child = BinarySearchTree(75)
        bst.insert(child)
        self.assertEqual(bst.right, child)

    def test_insert_to_child_lesser(self):
        bst = BinarySearchTree(55)
        child1 = BinarySearchTree(25)
        child2 = BinarySearchTree(15)
        bst.insert(child1)
        bst.insert(child2)
        self.assertEqual(child1.left, child2)

    # def test_find(self):
    #     values = [21, 73, 14, 83, 67,23, 99, 104, 18,1]       
    #     bst = BinarySearchTree()
    #     for i in values:
    #         child = BinarySearchTree(i)
    #         bst.insert(child)
    #         if i == values[5]:
    #             node_to_find = child
    #     self.assertEqual(bst.find(values[5]), node_to_find)            

    # def test_in_order(self):
    #     values = [21, 73, 14, 83, 67,23, 99, 104, 18,1]       
    #     bst = BinarySearchTree()
    #     for i in values:
    #         bst.insert(BinarySearchTree(i))
    #     self.assertEqual(bst.in_order(), [21, 73, 14, 83, 67,23, 99, 104, 18,1].sort())                

    # def test_pre_order(self):
    #     values = [21, 73, 14, 83, 67,23, 99, 104, 18,1]       
    #     bst = BinarySearchTree()
    #     for i in values:
    #         bst.insert(BinarySearchTree(i))
    #     self.assertEqual(bst.pre_order(), [21, 14, 1, 18, 73, 67, 23, 83, 99, 104])                

    # def test_post_order(self):
    #     values = [21, 73, 14, 83, 67,23, 99, 104, 18,1]       
    #     bst = BinarySearchTree()
    #     for i in values:
    #         bst.insert(BinarySearchTree(i))
    #     self.assertEqual(bst.post_order(), [1, 18, 14, 23, 67, 83, 99, 104, 73, 21])                

if __name__ == '__main__':
    unittest.main()
            