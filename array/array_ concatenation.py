class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
    
    

if __name__ == "__main__":
        solution = Solution()
        print(solution.getConcatenation([1, 2, 3]))
        