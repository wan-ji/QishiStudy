# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/description/


# Method 1
# Runtime: 36 ms
# Memory Usage: 13.8 MB
# Your runtime beats 80.65 % of python3 submissions.
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        
        for i in range(max(0, num - 6), min(5, num + 1)):
            hours = []
            self.compute_numbers(i, 4, 3, 0, hours)
            minutes = []
            self.compute_numbers(num - i, 6, 5, 0, minutes)
            for hour in hours:
                for minute in minutes:
                    ans.append("%d:%02d" % (hour, minute))
        
        return ans
    
    def compute_numbers(self, i, total_digit, start_idx, number, res):
        if number > (11 if total_digit == 4 else 59):
            return
        if i == 0:
            res.append(number)
            return
        
        for idx in range(start_idx, i - 2, -1):
            self.compute_numbers(i - 1, total_digit, idx-1, number | (1 << idx), res)


# Method 2
# Runtime: 40 ms
# Memory Usage: 13.7 MB
# Your runtime beats 58.06 % of python3 submissions.
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        
        for i in range(max(0, num - 6), min(5, num + 1)):
            hours = self.compute_numbers(i, 4)
            minutes = self.compute_numbers(num - i,6)
            for hour in hours:
                for minute in minutes:
                    ans.append("%d:%02d" % (hour, minute))
        
        return ans
            
    def compute_numbers(self, i, tot_digit):
        if i == 0: return [0]
        min_num = (1 << i) - 1
        max_num = min(min_num << (tot_digit - i), 11 if tot_digit == 4 else 59)
        res = []
        for num in range(min_num, max_num + 1):
            if bin(num).count('1') == i:
                res.append(num)
        return res