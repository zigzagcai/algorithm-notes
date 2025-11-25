def quicksort_naive(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quicksort_naive(left)+middle+quicksort_naive(right)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 8, 7]
    arr = quicksort_naive(arr)
    print(f"sorted arr = {arr}", flush=True)