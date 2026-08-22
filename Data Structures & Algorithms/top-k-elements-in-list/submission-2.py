from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        lst = [[k, v] for k, v in hashmap.items()]
        sorted_lst = sorted(lst, key = lambda x: x[1], reverse = True)
        res = [item[0] for item in sorted_lst]
        return res[:k]