class Solution(object):
    def findBestValue(self, arr, target):
        import bisect
        diff = float('inf')
        res = 0
        arr.sort()
        val = []
        count = 0
        for i in arr:
            count += i
            val.append(count)
        for v in range(0,arr[-1] + 1):
            inx = bisect.bisect_right(arr,v)
            amount = v * (len(arr) - inx)
            if inx > 0:amount += val[inx-1]
            if diff > abs(amount - target):
                diff = abs(amount - target)
                res = v
        return res
val=Solution()
n,k=map(int,input().split())
A=list(map(int,input().split()))
print(val.findBestValue(A,k))
