def selection_sort(l):
    for i in range(0, len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

    return l

print(selection_sort([24, 2, 98, 23, 32, 0]))