'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def sliding_window_pattern(self, s):
        # Boundary Conditions(optional)
        if len(s) == 0:
            return 0
        
        # Initial
        slide_window = set()
        slide_window.add(s[0])
        max_length = 1
        start_idx, end_idx = 0, 1

        # Iterate the input
        while end_idx < len(s):
            # Expand the window
            char_in = s[end_idx]
            # Meet the condition to stop expansion
            while char_in in slide_window:
                # Process the current window
                char_out = s[start_idx]  
                slide_window.remove(char_out)     
                # Contract the window
                start_idx += 1
            slide_window.add(char_in)
            max_length = max(max_length, end_idx - start_idx + 1)
            end_idx += 1
        
        return max_length


if __name__ == '__main__':
    solver = Solution()
    params = {
        "s":"pwwkew"
    }
    print(solver.sliding_window_pattern(**params))
