class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        mini=float('inf')
        for i,val in enumerate(prices):
            result=max(result,val-mini)
            mini=min(mini,val)
        return result
        