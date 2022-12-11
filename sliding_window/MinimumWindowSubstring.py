'''
https://leetcode.cn/problems/minimum-window-substring/


'''
class Solution:
    def sliding_window_pattern(self, s, t):
        # Boundary Conditions(optional)
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        goal_cnt = len(t)
        for idx in counter_t:
            if counter_t[idx] > counter_s[idx]:
                return ""
    
        # Initial
        slide_window = Counter()
        start_idx, end_idx = 0, 0
        min_length = len(s)
        aim_arr = ""
        char_cnt = 0
        # Iterate the input
        while end_idx < len(s):
            char_in = s[end_idx]
            slide_window[char_in] += 1
            if slide_window[char_in] <= counter_t[char_in]:
                char_cnt += 1
            # Meet the condition to stop expansion
            while start_idx < len(s) and slide_window[s[start_idx]] > counter_t[s[start_idx]]:
                # Process the current window
                char_out = s[start_idx]
                slide_window[char_out] -= 1
                if slide_window[char_out] == 0:
                    slide_window.pop(char_out)
                # Contract the window
                start_idx += 1
            # Update the states
            if char_cnt == goal_cnt:
                if min_length >= end_idx - start_idx + 1:
                    min_length = end_idx - start_idx + 1
                    aim_arr = s[start_idx: end_idx+1]
            end_idx += 1


        return aim_arr

if __name__ == '__main__':
    solver = Solution()
    params = {
        "s": "a",
        "t": "a"
    }
    print(solver.sliding_window_pattern(**params))
