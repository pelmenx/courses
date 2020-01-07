# B is rotation A?
def is_rotation(a, b):
    pointer = -1
    if len(a) != len(b):
        return False
    for i in range(0, len(b)):
        if a[0] == b[i]:
            pointer = i
    if pointer != -1:
        for items in a:
            if items != b[pointer % len(b)]:
                return False
            pointer += 1
        return True
    else:
        return False


A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]

print(is_rotation(A, B))
