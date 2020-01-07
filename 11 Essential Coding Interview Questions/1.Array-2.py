# find common elements in A and B sortred arrays;


def common_elements(a, b):
    common_array = []
    pointer = 0
    if len(a) > len(b):
        for numbers in a:
            quit = 0
            for i in range(pointer, len(b)):
                if numbers == b[i]:
                    common_array.append(numbers)
                    pointer = i + 1
                    quit = 1
                    break
                elif numbers < b[i]:
                    pointer = i
                    quit = 1
                    break
            if quit == 0:
                return(common_array)
    else:
        for numbers in b:
            quit = 0
            for i in range(pointer, len(a)):
                if numbers == a[i]:
                    common_array.append(numbers)
                    pointer = i + 1
                    quit = 1
                    break
                elif numbers < a[i]:
                    pointer = i
                    quit = 1
                    break
            if quit == 0:
                return(common_array)
    return(common_array)


A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

print(common_elements(A, B))
