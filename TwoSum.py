class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {key:value for value,key in enumerate(nums)}
        return_list = []

        for i in range(len(nums)):
            want = target - nums[i]

            if ((want in dictionary) and (i != dictionary[want])):
                return_list.extend([i,dictionary[want]])
                break
        return return_list
