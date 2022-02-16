def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j]<l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
            j -= 1
    return l

print(insertion_sort([23, 34, 12, 9, 19]))
