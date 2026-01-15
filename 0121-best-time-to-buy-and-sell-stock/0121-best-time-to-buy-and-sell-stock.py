class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxp=0
        for p in prices:
            if p<minp:
                minp=p
            else:
                maxp=max(maxp,p-minp)
        return maxp
