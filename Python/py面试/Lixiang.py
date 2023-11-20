class Solution:
    def calweight(stones) -> int:
        # write code here
        num = len(stones)
        while num > 1:
            stones.sort()
            diff = stones[num-1] - stones[num-2]
            stones.pop()
            stones.pop()
            if diff != 0:
                stones.append(diff)
            num = len(stones)
            if num == 1:
                return stones[0]

        return 0
print(Solution.calweight([2,7,4,1,8,1]))