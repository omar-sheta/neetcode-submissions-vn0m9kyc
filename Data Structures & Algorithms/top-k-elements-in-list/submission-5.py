class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # I need to get the count of nums
        count = Counter(nums)

        # sort this dict based on values
        sorted_ordered_dict = OrderedDict(sorted(count.items(), key=lambda item: item[1], reverse = True))

        return list(sorted_ordered_dict.keys())[:k]


        
        
        
        












        
        
        
        
        
        
        
        
        
        
        
#         # first begin by counting occurences 
#         count = {}
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)

#         heap = []
#         # create a heap with only k elements, meaning that top k elements will stay.
#         for n in count.keys():
#             heapq.heappush(heap, (count[n], n))
#             if len(heap) > k:
#                 heapq.heappop(heap)


#         # append top k elements in list
#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])

#         return res
#         # for num in nums:
#         #     count[num] = 1 + count.get(num,0)
        
#         # heap = []

#         # for num in count.keys():
#         #     heapq.heappush(heap, (count[num], num))
#         #     if len(heap)>k:
#         #         heapq.heappop(heap)

#         # res = []
#         # for i in range(k):
#         #     res.append(heapq.heappop(heap)[1])
#         # return res

