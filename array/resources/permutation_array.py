class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in range(0, len(nums)):
            new_list.append(nums[nums[i]])
            
        return new_list
    
    
if __name__ == "__main__":
        solution = Solution()
        print(solution.buildArray([5,0,1,2,3,4]))
        