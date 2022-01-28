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
                    
            