#reverse an array
##def rev_array(arr):
##    left, right=0, len(arr)-1
##
##    while left<right:
##        arr[left],arr[right]=arr[right],arr[left]
##        left+=1
##        right-=1
##    return arr
##
##
##print(rev_array([1,2,3,4,5]))
##    

##find max and min
##def find_max_min(arr):
##    return max(arr), min(arr)
##
##print(find_max_min([1,8,99,0,2]))


####maximun subarray sum
##def max_subarray(arr):
##    max_sum=arr[0]
##    current_sum=arr[0]
##
##    for i in range(1, len(arr)):
##        current_sum=max(arr[i],current_sum+arr[i])
##        max_sum=max(max_sum, current_sum)
##
##    return max_sum
##print(max_subarray([1,2,3,-9, 4,5]))


##Quick sort--rearrange ele around pivot
##def quick_sort(arr):
##    if len(arr)<=1:
##        return arr
##    pivot=arr[len(arr)//2]
##
##    left = [x for x in arr if x<pivot]
##    right =[x for x in arr if x> pivot]
##    middle = [x for x in arr if x==pivot]
##
##    return quick_sort(left)+ middle + quick_sort(right)
##arr=[4,3,9,8,2]
##print(quick_sort(arr))



######################################################################
def switch_case(choice):
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday"
    }.get(choice, "Invalid choice")

print(switch_case(2))






















##########################################################
#practice
##def rev_array(arr):
##    left, right=0,len(arr)-1
##    while left < right:
##        arr[left], arr[right]=arr[right], arr[left]
##        left+=1
##        right-=1
##    return arr
##
##print(rev_array([1,2,3,4,5]))




