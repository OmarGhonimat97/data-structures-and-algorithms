from hashtable.hashtable import *

from trees.trees import BinaryTree, TNode


def tree_intersection(tree_1, tree_2):

    if not tree_1.root or not tree_2.root:
        return []

    ht = HashTable()
    t1 = tree_1.in_order()
    t2 = tree_2.in_order()

    for i in t1:
        if i in t2:
            ht.set(i, i)
    return ht.key()


if __name__ == "__main__":
    b1_tree = BinaryTree()
    b2_tree = BinaryTree()

    b1_tree.root = TNode(150)
    b1_tree.root.left = TNode(100)
    b1_tree.root.left.left = TNode(75)
    b1_tree.root.left.right = TNode(160)
    b1_tree.root.left.right.left = TNode(125)
    b1_tree.root.left.right.right = TNode(175)
    b1_tree.root.right = TNode(250)
    b1_tree.root.right.left = TNode(200)
    b1_tree.root.right.right = TNode(350)
    b1_tree.root.right.right.left = TNode(300)
    b1_tree.root.right.right.right = TNode(500)

    b2_tree.root = TNode(42)
    b2_tree.root.left = TNode(100)
    b2_tree.root.left.left = TNode(15)
    b2_tree.root.left.right = TNode(160)
    b2_tree.root.left.right.left = TNode(125)
    b2_tree.root.left.right.right = TNode(175)
    b2_tree.root.right = TNode(600)
    b2_tree.root.right.left = TNode(200)
    b2_tree.root.right.right = TNode(350)
    b2_tree.root.right.right.left = TNode(4)
    b2_tree.root.right.right.right = TNode(500)

    print(tree_intersection(b1_tree, b2_tree))
