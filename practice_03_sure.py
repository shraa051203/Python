#quick sort
##def quick_sort(arr):
##    if len(arr)<=1:
##        return arr
##    pivot=arr[len(arr)//2]
##
##    left=[x for x in arr if x<pivot]
##    right=[x for x in arr if x>pivot]
##    middle=[x for x in arr if x==pivot]
##
##    return quick_sort(left)+ middle+ quick_sort(right)
##arr=[9,4,6,9,0,4]
##print(quick_sort(arr))


##merge sort
##def merge_sort(arr):
##    if len(arr)<=1:
##        return arr
##
##    mid=len(arr)//2
##
##    left=merge_sort(arr[:mid])
##    right=merge_sort(arr[mid:])
##
##    result=[]
##    i=j=0
##
##    while i<len(left) and j<len(right):
##        if left[i]< right[j]:
##            result.append(left[i])
##            i+=1
##        else:
##            result.append(right[j])
##            j+=1
##            
##    result+=left[i:]
##    result+=right[j:]
##    return result
##
##arr=[7,3,5,0,6,4,8,6,7]
##print(merge_sort(arr))
##
##
##
##def merge_sort(arr):
##    if len(arr)<=1:
##        return arr
##
##    mid=len(arr)//2
##
##    left=merge_sort(arr[:mid])
##    right=merge_sort(arr[mid:])
##
##    result=[]
##    i=j=0
##
##    while i<len(left) and j<len(right):
##        if left[i]< right[i]:
##            result.append(left[i])
##            i+=1
##        else:
##            result.append(right[j])
##            j+=1
##
##        result+=left[i:]
##        result+=right[j:]
##        return result
##
##arr=[7,4,9,5,4,6,8]
##print(merge_sort(arr))



def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2

    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    result=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]< right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

        result+=left[i:]
        result+=right[j:]
        return result

arr=[7,8,4,3,0,2]
print(merge_sort(arr))
        
































