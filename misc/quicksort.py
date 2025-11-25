def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
            

def quicksort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quicksort(arr, low, part-1)
        quicksort(arr, part+1, high)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 8, 7]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print(f"sorted arr = {arr}", flush=True)
    