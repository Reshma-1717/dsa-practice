class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]
        delete = 0
        ans = arr[0]
        for i in range(1, len(arr)):
            x = arr[i]
            delete = max(keep, delete + x)
            keep = max(x, keep + x)
            ans = max(ans, keep, delete)
        return ans