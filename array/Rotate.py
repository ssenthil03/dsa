# Array rotation by Reversal Algorithm

arr = [1, 2, 3, 4, 5, 6, 7]
def reverseArray(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr


def rotateArray(arr, d):
    n = len(arr)
    
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
print(f"Before Rotation: {arr}")
rotateArray(arr, 2)
print(f"After Rotation: {arr}")

    