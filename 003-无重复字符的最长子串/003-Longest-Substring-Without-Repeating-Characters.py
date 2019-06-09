import sys
import io

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        max_length = 0
        left = 0
        right = 0
        while (right < len(s)):
            if s[right] not in check:
                check.add(s[right])
                right += 1
                max_length = max(right - left, max_length)
            else:
                check.remove(s[left])
                left += 1
        return max_length
        

def main():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            
            ret = Solution().lengthOfLongestSubstring(line)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()