#13. Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ints = []
        for l in s:
            if l == 'I':
                ints.append(1)
            if l == 'V':
                ints.append(5)
            if l == 'X':
                ints.append(10)
            if l == 'L':
                ints.append(50)
            if l == 'C':
                ints.append(100)
            if l == 'D':
                ints.append(500)
            if l == 'M':
                ints.append(1000)
                
        for i in range(len(ints)-1):
            if ints[i] < ints[i+1]:
                ints[i+1] = ints[i+1]-ints[i]
                ints[i] = 0
        
        
                    
        return sum(ints)

                    
# 14. Longest Common Prefix 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        short = min(strs, key=len)
        prefix = ""
        if strs == False:
            return prefix
         
        if short.isalpha() == True:
           
            if len(strs) == 1:
                return strs[0]
    
            else:
                i = len(short)
                while i > 0:
                    counter = 0
                    for word in strs:
                        if word[:i] == short[:i]:
                            counter += 1
                        if counter == len(strs):
                            return short[:i]
                    i = i - 1
                return prefix
                    
        else:
            return prefix


#Leetcode #1 slow version
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        for i1, num in enumerate(nums):
            for i2, number in enumerate(nums):
                if i1 != i2 and num + number == target:
                    return[i1, i2]
                
        
            
#Leetcode #1 smokin fast version
# 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        while i < len(nums):
            addend = target - nums[i]
            sub_nums = nums[i+1:]
            
            if addend in sub_nums:
                return[i, sub_nums.index(addend) + i + 1]
            
            i += 1
            

#Leetcode 9 Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x_ = str(x)
        
        if x_[:] == x_[::-1]:
            return True
        else:
            return False
                
               
            
            
            
            
            
            
            
            
          