class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        begin=0
        end=0
        str_dict={}
        str_len=len(s)
        for end in range(str_len):
            cal_end=end
            if s[end] in str_dict:
                begin=max(begin,str_dict[s[end]]+1)
                if begin>str_dict[s[end]]:
                    cal_end=end
                else:
                    cal_end=end-1
            str_dict[s[end]]=end
            maxlen=max(maxlen,cal_end- begin+1)
            print(begin,end,cal_end,maxlen)
        return maxlen
solu=Solution()
s=solu.lengthOfLongestSubstring("aabaab!bb")
print(s)

'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        begin=0
        end=0
        str_dict={}
        str_len=len(s)
        while end<str_len:
            temp_end=str_dict.get(s[end])
            str_dict[s[end]]=end
            if temp_end is not None:
                maxlen=max(maxlen,end-begin)
                begin=max(begin,temp_end+1)
            end=end+1
        maxlen=max(maxlen,end-begin)
        return maxlen
solu=Solution()
s=solu.lengthOfLongestSubstring("pwwkew")
print(s)
'''