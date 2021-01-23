# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Given a tree, find the largest tree/subtree that is a BST.
#
# Given a tree, return the size of the largest tree/subtree that is a BST.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


a = Node(50)
b = Node(25)
c = Node(75)
d = Node(12)
e = Node(37)
f = Node(67)
g = Node(87)
h = Node(80)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
g.right = h


def deepest_node(root_):
    def deepest_node_inside(root, depth=0):
        if not root.right and not root.left:
            return root, depth
        depth_right = depth
        if root.right:
            if root.right.arg >= root.arg and root.right.arg <= root_.arg:
                root_right, depth_right = deepest_node_inside(root.right, depth + 1)
            else:
                print(root.arg)
                print(123)
                depth_right = 0
                root_right, depth_right = deepest_node_inside(root.right, depth + 1)
        depth_left = depth
        if root.left:
            if root.left.arg <= root.arg and root.left.arg <= root_.arg:
                root_left, depth_left = deepest_node_inside(root.left, depth + 1)
            else:
                depth_left = 0
                root_left, depth_left = deepest_node_inside(root.left, depth + 1)
        if depth_left > depth_right:
            return(root_left, depth_left)
        else:
            return(root_right, depth_right)

    print(deepest_node_inside(root_)[0].arg)


deepest_node(a)
