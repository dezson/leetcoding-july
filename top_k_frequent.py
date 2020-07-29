from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums).items()
        for num, freq in counter:
            bucket[freq].append(num)

        flat_list = []
        for sublist in bucket[::-1]:
            for item in sublist:
                flat_list.append(item)
        return flat_list[:k]

    def topKFrequentDict(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] +=1

        nums = sorted(d.items(), key=lambda item : item[1] , reverse=True)
        return [y[0] for y in nums[:k]]
