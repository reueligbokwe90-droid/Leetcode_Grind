class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for _ in range(k):
            # find the key with max count
            num = max(count, key=count.get)
            res.append(num)
            # remove it so it won't be chosen again
            del count[num]
        return res