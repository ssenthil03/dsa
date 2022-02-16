def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        R = lst[mid:]
        L = lst[:mid]

        merge_sort(L)

        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[i]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
    return lst

print(merge_sort([12, 11, 13, 5, 6, 7]))
    