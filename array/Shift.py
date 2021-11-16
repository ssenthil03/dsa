# Shifting Elements to the Right side

def rightShift(arr, d):
    n = len(arr)
    i = 0
    while i <= d:
        temp = arr[n-1]
        for j in range(n-1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = temp
        i += 1
    return arr



# Shifting Elements to the Left Side

def leftShift(arr, d):
    n = len(arr)
    i = 0
    while i <= d:
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
        i += 1
    return arr



arr1 = [1, 2, 3, 4, 5]
print(f"Before Shifting: {arr1}\n")

rightShift(arr1, 2)
print(f"After Shifting: (Right){arr1}\n")

arr2 = [6, 7, 8, 9, 10]
print(f"Before Shifting: {arr2}\n")


leftShift(arr2, 2)
print(f"After Shifting: (Left){arr1}\n")