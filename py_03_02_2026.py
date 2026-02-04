def my_decorator(func): # asli function yaha ayega
    print("you are at decorator decorator define ho gaya hain !")
    def wraper(*args,**kwargs): # argument ko handle karne ke liye
        print("your are inside the inner decorator function chalne se pahle yeh chalne wala hain ")
        result = func(*args,**kwargs)
        print("function chalne ke baad wala wala kam ")
        return result
        
    return wraper # sirf reference return ho gaya hain call nhi!
    
@my_decorator
def sum_of(a,b):
    return a+b
    
# print(sum_of(10,20))
"""
FizzBuzz: 1 se 100 tak print karo. Agar number 3 se divisible hai toh "Fizz", 5 se hai toh "Buzz", aur dono se hai toh "FizzBuzz"."""

# n = int(input("enter limits to print"))

def fizzbuzz(n:int):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5==0:
            print("fizzbuzz")
        elif i %3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    
# fizzbuzz(n)

"""
Prime Number Check: Ek function likho jo bataye number prime hai ya nahi (optimized way mein).
"""
def is_prime(n:int):
    lim = n//2 +1
    check = 0
    for i in range(3,lim+1):
        if n % i == 0:
            check += 1
    return "prime" if check < 1 else "non-prime"
# print(is_prime(7))

"""Factorial using Recursion: Recursion ka dimaag kholne ke liye best hai."""

def factorial(n:int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
"""Fibonacci Series: Pehle $n$ numbers print karo."""
def febonacci(n:int):
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b 

"""Reverse a String: Bina [::-1] use kiye loop se reverse karo."""
def reverse(s:str):
    temp = ""
    for _ in s:
        temp = _ + temp
    return temp

"""Find Largest in List: Bina max() function use kiye list ka sabse bada number dhoondo."""
def largest_in_list(l:list):
    max_num = 0
    for i in l:
        if i > max_num:
            max_num = i
    return max_num

"""Palindrome Check: Check karo "radar" ya "level" ulta karne par same hai ya nahi."""
def check_for_palindrome(s:str):
    return "Pallindrome" if s == s[::-1] else "not pallindrome"

"""Remove Duplicates: Ek list se duplicates hatao bina set() use kiye."""
def remove_duplicates(l:list):
    non_dup = []
    for i in l:
        if i not in non_dup:
            non_dup.append(i)
        else:
            pass
    return non_dup

"""Anagram Check: Do strings same characters use karti hain ya nahi? (e.g., "listen" aur "silent")"""
def check_for_anagram(s1:str,s2:str):
    if sorted(s1) == sorted(s2):
        return "annagram"
    else:
        return "not annagram"
    
"""Character Frequency: Ek string mein har character kitni baar aaya, dictionary mein store karo."""
def counter(s:str):
    ans = {}
    for i in s:
        ans[i]=ans.get(i,0)+1
    return ans

"""Find Second Largest: List mein dusra sabse bada number dhoondo (single pass mein)."""
def find_second_last(l:list):
    max_n = 0
    second = 0
    for i in l:
        if i > second:
            if i > max_n:
                second = max_n
                max_n = i
            else:
                second = i
        else:
            pass
    return second


"""List Flattening: Agar list ke andar list ho [1, [2, 3], 4], toh use single list [1, 2, 3, 4] banao."""

def get_all_in_one(l1:list):
    ans = []
    for i in l1:
        if isinstance(i, list):
            for j in i:
                ans.append(j)
        else:
            ans.append(i)
    return ans

"""Missing Number: 1 se $n$ tak ki list mein ek number missing hai, use dhoondo."""
l1 = [1, 2, 3, 5]
n = 5
import math
def find_missing(l1:list,n:int):
    l = sum(l1)
    total = (n)* ((n+1)/2)
    return int(total - l)

"""Valid Parentheses: Check karo brackets sahi se close ho rahe hain ya nahi ({[]}). (Stack logic)."""

def valid_paranthis(s:str):
    data = {"}":"{",
        ")":"(",
        "]":"["
    }
    stack=[]
    for i in s:
        if i in data.values():
            stack.append(i)
        elif i in data:
            if not stack or stack.pop() != data[i]:
                return False
    return len(stack) == 0

"""Move Zeroes to End: Ek list [0, 1, 0, 3, 12] ko [1, 3, 12, 0, 0] banao bina extra list create kiye."""
def move_zeros(l:list):
    
    non_zeros = []
    zeros = []
    for i in l:
        if i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    return non_zeros + zeros

def adv_move_zeros(l:list):
    return [i for i in l if i !=0] + [0] * l.count(0)

"""Two Sum Problem: List mein se wo do numbers dhoondo jinka sum ek "Target" ke barabar ho"""
def two_sum(nums: list, target: int):
    seen = {}

    for i, num in enumerate(nums):
        rem = target - num
        if rem in seen:
            return [seen[rem], i]
        seen[num] = i
    return [] 

"""Group Anagrams: Strings ki list ko groups mein baanto (e.g., ['eat', 'tea', 'tan', 'nat'] -> [['eat', 'tea'], ['tan', 'nat']])."""

list1 = ['eat', 'tea', 'tan', 'nat']

def sor_char(l:list):
    ans_dict = {}
    
    for i in list1:
        if "".join(sorted(i)) not in ans_dict:
            ans_dict["".join(sorted(i))] = [i]
        else:
            ans_dict["".join(sorted(i))].append(i)
        
    return ans_dict.values()

"""Interval Merging (Inventory Logic): Agar do discount offers overlap ho rahe hain, toh unhe merge karo."""

def merge_list(disc:list):
    answer = []
    disc.sort()
    start,end = disc[0]
    for i in range(1,len(disc)):
        if disc[i][0] < end:
            end = max(end,disc[i][1])
        else:
            answer.append([start,end])
            start,end = disc[i]
    answer.append([start,end])
    return answer


"""Memoization (Optimization): Kisi bhi slow function ko cache (decorator use karke) fast banao"""

"""Locker Challenge: 100 lockers hain aur 100 students. Har student apne number ke multiple wale lockers ko toggle (khulna/band) karta hai. Anth mein kitne lockers khule rahenge?"""