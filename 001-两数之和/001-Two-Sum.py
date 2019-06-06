from typing import List
import json
import sys
import io

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for index,num in enumerate(nums):
            if num in temp:
                return [temp[num], index]
            else:
                temp[target - num] = index

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()