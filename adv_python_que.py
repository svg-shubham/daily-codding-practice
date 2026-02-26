# Two Sum (Target sum find karein)	Input: [2, 7, 11], Target: 9 → Output: [0, 1]
# normal logic
def target_sum(arr:list[int],fsum:int)->list[int]:
    result = []
    for i in range(len(arr)):
        target = fsum - arr[i]
        for j in range(len(arr)):
            if i == j:
                pass
            else:
                if arr[j] == target:
                    result.append(i)
                    result.append(j)
                
    return list(set(result))
# print(target_sum([2, 7, 11],9))

# advance way
def target_sum(arr:list[int],fsum:int)->list[int]:
    seen = {}
    for i, num in enumerate(arr):
        complement = fsum - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
# print(target_sum([2, 7, 11],9))

# Find Missing Number [1, 2, 4, 5] (1 to 5 range) → Output: 3
def find_missing_number(arr:list[int])->int:
    n = len(arr) + 1 
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
# print(find_missing_number([1, 2, 4, 5]))
# Merge Two Sorted Lists	Input: [1, 3], [2, 4] → Output: [1, 2, 3, 4]
def merge_two_list(arr1:list[int],arr2:list[int])->list[int]:
    return sorted(arr1+arr2)

# two pointer approach for this
def merge_two_list(arr1:list[int],arr2:list[int])->list[int]:
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
    
# print(merge_two_list([1, 3], [2, 4]))
# Find Second Largest	Input: [10, 20, 4, 45] → Output: 20
def find_second_larget(arr:list[int])->int:
    first = 0
    second = 0
    for num in arr:
        if num > second:
            if num < first:
                second = num
            else:
                second = first
                first = num
        
    return second

# Rotate Array (k steps)	Input: [1, 2, 3], k=1 → Output: [3, 1, 2]
def rotate_arr_k(arr:list[int],k:int)->list[int]:
    return arr[k:]+arr[:k]

# Binary Search	Input: [1, 2, 3, 4, 5], Search: 4 → Output: Index 3
def lenear_serach(arr:list[int],k:int)->int:
    for ind,num in enumerate(arr):
        if num == k:
            return ind
        else:
            pass

# binary search
def binary_search(arr: list[int], k: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == k:
            return mid        
        elif arr[mid] < k:
            low = mid + 1     
        else:
            high = mid - 1
    return -1

# Intersection of 2 Arrays	Input: [1, 2], [2, 3] → Output: [2]
def intersection_of_array(arr1:list[int],arr2:list[int])->int:
    arr1.sort()
    arr2.sort()
    result = []
    for i in arr1:
        for j in arr2:
            if i==j:
                result.append(i)
            
    return result

# advanced way
def intersection_of_array(arr1:list[int],arr2:list[int])->int:
    return list(set(arr1) & set(arr2))

# First Unique Character	Input: "leetcode" → Output: "l"
from collections import Counter
def first_unique_charector(s:str)->str:
    s1 = Counter(s)
    for i in s:
        if s1[i]== 1:
            return i
    
    return None

# valid parantheses
def is_valid_parentheses(s:str)->bool:
    data = {"}":"{","]":"[",")":"("}
    stack =[]
    for char in s:
        if char in data:
            top_ele = stack.pop()
            if data[char] != top_ele:
                return False
        else:
            stack.append(char)
    return not stack
    
# print(is_valid_parentheses("([)]"))


