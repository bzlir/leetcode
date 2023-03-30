class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for idx, val in enumerate(s):
            countS[val] = countS.get(val, 0) + 1
            countT[t[idx]] = countT.get(t[idx], 0) + 1

        for item in countS:
            if countS[item] != countS.get(item,0):
                return False
            
        return True
            


if __name__ == '__main__':
    solver = Solution()
    params = {
        "s" : "anagram", 
        "t" : "nagaram"
    }
    print(solver.isAnagram(**params))