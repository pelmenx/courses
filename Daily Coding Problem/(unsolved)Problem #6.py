# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node. Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index)
# which returns the node at index.
# if using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and dereference_pointer functions
# that converts between nodes and memory addresses.


def node_to_index(array):
    index_array = []
    for items in array:
        index_array.append(id(items))
    return index_array


def doubly_linked_list(index_array):
    doubly_linked_array = []
    for i in range(0, len(index_array)):
        if i == 0 or i == len(index_array) - 1:
            doubly_linked_array.append(index_array[i])
        else:
            doubly_linked_array.append(index_array[i - 1] ^ index_array[i + 1])
    return doubly_linked_array


node_list = [1, 2, 3, 4, 5]
index_node_list = node_to_index(node_list)
doubly_index_node_list = doubly_linked_list(index_node_list)

print(index_node_list)
print(doubly_index_node_list)
print(doubly_index_node_list[0] ^ doubly_index_node_list[2])
