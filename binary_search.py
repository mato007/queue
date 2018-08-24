def binary_search(a, x):
    begin, end = 0, len(a)


    while end - begin > 1:
        mid = (begin + end) // 2

        if a[mid] > x:
            end = mid
        else:
            begin = mid

    return a[begin] == x




a = [0, 1, 3, 3, 5, 7, 9, 9, 11, 13]

for i in range(5):
        print("Is %d in array? %s" % (i, binary_search(a, i)))


