def binary_search(target, arr, left, right):
    if arr[right] == target:
        return right
    if left > right:
        return right
    mid = (left + right) // 2
    if arr[mid] > target:
        return binary_search(target, arr, left, mid - 1)
    else:
        return binary_search(target, arr, mid + 1, right)
    
n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

print(' '.join([str(binary_search(v, arr2, i,n-1)-i) for i,v in enumerate(arr1)]))