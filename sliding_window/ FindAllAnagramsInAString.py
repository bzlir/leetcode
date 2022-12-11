'''
https://leetcode.cn/problems/find-all-anagrams-in-a-string/
'''
class Solution:
    def sliding_window_pattern(self, s, p):
        # Boundary Conditions(optional)
        # if len(s) == 0:
        #     return 0
        
        # Initial
        from collections import Counter
        slide_window = Counter(p)
        index_list = list()
        start_idx, end_idx = 0, len(p)
        # Iterate the input
        while end_idx <= len(s):
            char_in = Counter(s[start_idx: end_idx])
            # Meet the condition to stop expansion
            if char_in == slide_window:
                # Process the current window
                index_list.append(start_idx)     
                # Contract the window
                # the size of the window is fixed
            # Expand the window
            end_idx += 1
            start_idx = end_idx - len(p)
        
        return index_list


if __name__ == '__main__':
    solver = Solution()
    params = {
        "s": "cbaebabacd",
        "p": "abc"
    }
    print(solver.sliding_window_pattern(**params))
