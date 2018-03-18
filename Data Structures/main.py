from BinaryTree import BinaryTree

tree = BinaryTree("Test")


tree.addLeft("Left")
tree.addLeft("Right")

myLeft = tree.get_left_child()
print(myLeft.get_data())