
import math
from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def getDistance(x,y):
            return math.sqrt(x**2 + y**2)

        d_to_p = defaultdict(list)
        distances = []

        result = []

        for point in points:

            x, y = point
            d = getDistance(x,y)

            d_to_p[d].append(point)
            print(d_to_p[d])
            distances.append(d)

        heapq.heapify(distances)

        for _ in range(K):

            min_d = heapq.heappop(distances)
            result.append(d_to_p[min_d].pop())

        return result

# another way of solving it following the same idea using heaps

import math
from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def getDistance(x,y):
            return math.sqrt(x**2 + y**2)

        result = []
        for point in points:

            x, y = point
            d = getDistance(x,y)

            if len(result) < K:
                heapq.heappush(result, ((-1)*d, point))
            else:
                heapq.heappushpop(result, ((-1)*d, point))


        return [t[1] for t in result]