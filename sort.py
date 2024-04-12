def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        for j in range(0, n-i-1):
         
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


#Test: 
if __name__ == "__main__":
    test_array = [4, 5 ,1, 8, 2, 12, 457, 5, 7, 6797]
    print(test_array)
    sorted_arry = bubble_sort(test_array)
    
    print(sorted_arry)