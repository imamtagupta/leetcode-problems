

#################################
# 1929. Concatenation of Array  #
#################################

# leetcode link: https://leetcode.com/problems/concatenation-of-array/description/


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    

# NOTE: There is a hack there where we can directly modify leetcode files to faster the process and reduce processing time.
# a = open("user.out", "w")
# for line in stdin:
#     nums = ','.join([n.strip() for n in (line.rstrip()[1:]).rstrip()[:-1].split(',')])
#     print(f'[{nums},{nums}]',sep="",file=a)
# exit()

# PS: But i guess this can be done only for simplest problems!!