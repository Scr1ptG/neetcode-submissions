class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        length = 0

        for num in nums:
            seq = 0
            if num - 1 in hashmap:
                continue
            
            while num + seq in hashmap:
                seq += 1
        
            length = max(length, seq )
        
        return length