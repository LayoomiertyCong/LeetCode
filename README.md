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
## 两数相加
* **Python部分知识性说明**

    ```Python
    class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    ```
    * 此部分为Python中链表的节点定义，初始化时node=ListNode(x)即可
    * Python中NULL(空字符)，None(空对象)，所以如果p==None他是没有属性的,即p.val and p.next都是不存在的
* **解题部分**

    ```Python
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p=l1
        q=l2
        carry=0
        first_flag=1
        head=None
        c_node=None
        while p!=None or q!=None or carry!=0:
            val1=0
            val2=0
            if p!=None:
                val1=p.val
                p=p.next
            if q!=None:
                val2=q.val
                q=q.next
            temp_sum=val1+val2+carry
            if temp_sum>=10:
                carry=1
                temp_sum=temp_sum%10
            else:
                carry=0
            temp_node=ListNode(temp_sum)
            if first_flag==1:
                c_node=temp_node
                head=temp_node
                first_flag=0
            else:
                c_node.next=temp_node
                c_node=c_node.next
        return head
    ```
    * 提前预留好最终链表的头节点head，以及每一步标记节点c_node，进位代表carry
    * while的循环判定，只要没加完（链表指针至少有一个不为空/仍然存在进位），就继续进行循环
    * 每一步判定是否有一个是空，此处注意None是没有p.val以及p.next的
    * 两数与上一步进位相加、计算有无进位、节点赋值并添加到最终链表中    
## 无重复字符的最长子串

