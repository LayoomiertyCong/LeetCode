# LeetCode
## 两数之和
* **函数定义部分**
    
    ```Python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    ```
    * 函数参数列表中的（:内容）意味着对参数进行注解
    * 函数参数列表后添加（->）指的是返回值的类型

* **解题部分**
    * 第一种方法：暴力拆解

        ```Python
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            for j in range(i+1,num_len):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
        ```
        * 显然最无脑的方法，超出时间限制
    * 第二种方法：一次循环在下面利用index功能

        ```Python
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            temp_num=target-nums[i]
            if temp_num in nums[i+1:]:
                j=nums[i+1:].index(temp_num)+i+1
                return [i,j]
        return []
        ```
        * 就此我们可以引申出下一种方法，这个方法中，一方面查后面的如果都是最差情况就很难受，所以我们可以查在nums[:i]中是否有
    * 第三种方法：仍然使用index功能但是在nums[:i]中寻找
        
        ```Python
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len=len(nums)
        for i in range(num_len):
            temp_num=target-nums[i]
            if temp_num in nums[:i]:
                j=nums[:i].index(temp_num)
                return [j,i]
        return []
        ```
        * 目前能够优化的就只有index部分 map的内部实现实际上就是hash，所以用hash存num[:i]
    * 第四种方法：hash表存储num[:i]

        ```Python
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
        ```
