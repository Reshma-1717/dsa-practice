class Solution:
    def findSubsets(self,nums,ind,ds,ans):
        ans.append(list(ds))
        for i in range(ind,len(nums)):
            ds.append(nums[i])
            self.findSubsets(nums,i+1,ds,ans)
            ds.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [];ds = []
        self.findSubsets(nums,0,ds,ans)
        return ans