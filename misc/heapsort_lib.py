import heapq

def heapsort_lib(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 8, 7]
    arr = heapsort_lib(arr)
    print(f"sorted arr = {arr}", flush=True)