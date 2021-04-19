class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1 or len(nums) == 0:
            return [nums]
        c = []
        s = set()
        for i in range(len(nums)):
            temp = nums[0:i] + nums[i+1:] if i is not (len(nums)-1) else nums[:i]
            if nums[i] in s: # if elements already in set(), ignore it
                continue
            else:
                s.add(nums[i])
            for res in self.permute(temp):
                c.append([nums[i]] + res)
        return c


sol = Solution()
print(sol.permute([1, 2, 3]))
