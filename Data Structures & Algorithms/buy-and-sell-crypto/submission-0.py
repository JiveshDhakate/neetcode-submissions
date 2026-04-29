class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        result=0
        for i in prices:
            min_price=min(i,min_price)
            diff=i-min_price
            result=max(result,diff)
        return result

        