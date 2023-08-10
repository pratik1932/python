#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# solution

length=int(input("Enter the number of integers in array:"))
i=0
numbers=[]
output=[]
while(i<length):
    numbers.append(int(input(f"Enter number {i+1}:")))
    i+=1
target=int(input("Enter target:"))
i=0
j=1
flag=0
while(i<length-1):
    while(j<length):
        if numbers[i]+numbers[j]==target:
            output.append(i)
            output.append(j)
            flag=1
            break
        else:
            j+=1
    else:
        i+=1
        j=i+1
    if flag==1:
        break
print(output)

# question 2:
#
# Given an integer x, return true if x is a  palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# solution
#
number=input("Enter integer to check wether it is pallindrome or  not :")
if number==number[::-1]:
    print(True)
else:
    print(False)

# question 3:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# constraints
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# solution:

length=int(input("Enter the number of strings in array:"))
i=0
strings=[]
prefix_char=[]
while(i<length):
    strings.append(input(f"Enter string {i+1}:").lower())
    i+=1
first_str=strings[0]
second_str=strings[1]

if len(first_str)<len(second_str):
    small_length=len(first_str)
else:
    small_length=len(second_str)
i=0
while(i<small_length):
    if first_str[i]==second_str[i]:
        prefix_char.append(first_str[i])
        i+=1
    else:
        break
prefix="".join(prefix_char)
if prefix!="":
    j=2
    while(j<length):
        if strings[j].startswith(prefix):
            j+=1
        else:
            prefix_char.pop()
            prefix="".join(prefix_char)
            if prefix=="":
                print("\"\"")
                break
    else:
        print(prefix)
else:
    print("\"\"")


# question 4:
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
#needle is not part of haystack.


# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0\

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# solution
haystack=input('Enter haystack string:').lower()
needle=input("Enter needle string:").lower()
output=haystack.find(needle)
print(output)

# question 5:
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, #return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.(not considered)

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# solution:

length=int(input("Enter the number of integers in sortd arrray:"))
i=0
numbers=[]
while(i<length):
    numbers.append(int(input(f"Enter number {i+1}:")))
    i+=1
target=int(input("enter target:"))
if target in numbers:
    index=numbers.index(target)
    print(index)
else:
    numbers.append(target)
    numbers.sort()
    index=numbers.index(target)
    print(index)

# question 6:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal  substring  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# solution

string=input("enter string:")
split_list=string.split()
max_length=0
for word in split_list:
    if len(word)>=max_length:
        max_length=len(word)
else:
    print(max_length)

# question 7:
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the #integer. The digits are ordered from most significant to least significant in left-to-right order. The large    # integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# Constraints:
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# solution:

length=int(input("enter number of digits in integer:"))
i=0
digits=[]
output=[]
while(i<length):
    digits.append(input(f"Enter digit {i+1}:"))
    i+=1
number=int("".join(digits))
number+=1
number=str(number)
output.extend(number)
print(output)

# question 8:

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# solution:1(using built in functions):

a=input("Enter 1st binary:")
b=input("Enter 2nd binary:")
output=str(bin(int(a,2)+int(b,2)))[2::]
print(f"\"{output}\"")

# solution:2 (without using built in functions):

def binarytodecimal(num):
    i=-1
    num_int=0
    count=0
    range=-(len(num))

    while(i>=range):
        digit=int(num[i])

        if digit==1:
             num_int=num_int+2**count
             i-=1
             count+=1
        else:
            i-=1
            count+=1
    return num_int
def decimaltobinary(num):
    sum_bin=""
    while(num!=0):
        rem=num%2
        sum_bin=sum_bin+(str(rem))
        num//=2
    return sum_bin[::-1]

num1_bin=input("Enter 1st binary:")
num2_bin=input("Enter 2nd binary:")
num1_int=binarytodecimal(num1_bin)
num2_int=binarytodecimal(num2_bin)
sum_int=num1_int+num2_int
sum_bin=decimaltobinary(sum_int)
print(f"\"{sum_bin}\"")

# quesstion 9:

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all #non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and #numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# solution:

def ispallindrome (s):
    s=s.lower()
    alphanumeric_char=[]
    if not s.isalnum():
        for char in s:
            if char.isalnum():
                alphanumeric_char.append(char)
        else:
          s="".join(alphanumeric_char)
          if s==s[::-1]:
             return True
    else:
        if s==s[::-1]:
            return True
s=input("Enter string to check whether it is pallindrome or not:")
result=ispallindrome(s)
print(result)

# question 10:

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# solution:

def singlenumber(nums):
    for num in nums:

        for num in nums:
            if nums.count(num)==1:
                return num
length=int(input("Enter thre number of inegers in array:"))
i=0
nums=[]
while(i<length):
    nums.append(int(input(f"enter number {i+1}")))
    i+=1
single_num=singlenumber(nums)
print(single_num)

# question 11:

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# solution

# def missingnum(nums):
#     Range = len(nums) + 1
#     for num in range(Range):          #less efficient ,more runtime
#         if num not in nums:
#             return num
 # OR
def missingnum(nums):
    nums.sort()
    i=0
    while(i<len(nums)):              #more efficient,less runtime
        if i!=nums[i]:
            return i
        else:
            i+=1
    else:
        return i
length=int(input("Enter number of integers in array:"))
i=0
nums=[]
while(i<length):
    nums.append(int(input(f"Enter numbre{i+1}:")))
    i+=1
missing_num=missingnum(nums)
print(missing_num)
