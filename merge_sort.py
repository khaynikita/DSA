def merge_sorted(arr1, arr2):
    i=j=0
    merged_array=[]
    while(i<len(arr1) and (j<len(arr2))):
        if(arr1[i]<arr2[j]):
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        merged_array.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        merged_array.append(arr2[j])
        j+=1
    print(merged_array)
merge_sorted([1,2,3,0,0,0],[1,2,3])

# def merge_sort(arr):

#     if len(arr)==1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     left=merge_sort(left)
#     right=merge_sort(right)
#     return (merge_sorted(left,right))
# result=merge_sort([2,99,34,21,2,34,700])
# print(result)