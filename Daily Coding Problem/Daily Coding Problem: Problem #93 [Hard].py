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
class Node_list(type):
    instances = list()

    def __call__(cls, *args, **kwargs):
        instance = super(Node_list, cls).__call__(*args, **kwargs)
        cls.instances.append(instance)
        return instance


class Node(object, metaclass=Node_list):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def find_valid_BST(root_list):
    def subtree(root):
        if root:
            yield root.arg
            if root.right:
                yield from subtree(root.right)
            if root.left:
                yield from subtree(root.left)

    def deepest_node_inside(root, depth=0):
        if not root.right and not root.left:
            return root, depth
        depth_right = depth
        if root.right:
            if root.right.arg >= root.arg:
                root_right, depth_right = deepest_node_inside(root.right, depth + 1)
            else:
                raise Exception
        depth_left = depth
        if root.left:
            if root.left.arg <= root.arg:
                root_left, depth_left = deepest_node_inside(root.left, depth + 1)
            else:
                raise Exception
        if depth_left > depth_right:
            return(root_left, depth_left)
        else:
            return(root_right, depth_right)

    max_deapth = 0
    root_ = None
    for instance in root_list:
        for node in subtree(instance.left):
            if node > instance.arg:
                continue
        for node in subtree(instance.right):
            if node < instance.arg:
                continue
        try:
            _, depth_ = deepest_node_inside(instance)
            if depth_ >= max_deapth:
                max_deapth = depth_
                root_ = instance
        except Exception:
            pass
    return root_, max_deapth


a = Node(50)
b = Node(25)
c = Node(75)
d = Node(12)
e = Node(37)
f = Node(62)
g = Node(87)
h = Node(80)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
g.right = h

assert find_valid_BST(Node.instances) == (b, 1)
