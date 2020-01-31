#暴力拆解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            for j in range(i+1,num_len):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
#用list的查找功能
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            temp_num=target-nums[i]
            if temp_num in nums[i+1:]:
                j=nums[i+1:].index(temp_num)+i+1
                return [i,j]
        return []

#在nums[:i]中用index功能：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            temp_num=target-nums[i]
            if temp_num in nums[:i]:
                j=nums[:i].index(temp_num)
                return [j,i]
        return []

#用hash表的方式存储num[:i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash={}
        num_len=len(nums)
        for i in range(num_len):
            temp_num=target-nums[i]
            if temp_num in nums_hash:
                j=nums_hash[temp_num]
                return [j,i]
            nums_hash[nums[i]]=i
        return []
