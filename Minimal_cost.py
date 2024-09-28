# Q. There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone
# exa. Input: k = 3, arr[]= [10, 30, 40, 50, 20]
# Output: 30
# Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

class Solution:
    def minimizeCost(self, k, arr):
        # code here
        # if k==0:
        #     return arr[0]
            
        # total_cost = 0
            
        # for i in range(k):
        #     count = abs(arr[i] - arr[i + 1])
        #     result = abs(arr[i + 1] - count)
            
        #     total_cost += count + result

        # return total_cost
        
       
            n = len(arr) 
            total_cost = [float('inf')] * n
            total_cost[0] = 0  

            for i in range(n):
                for j in range(i + 1, min(i + k + 1, n)):
                    cost = abs(arr[i] - arr[j])
                    total_cost[j] = min(total_cost[j], total_cost[i] + cost)

            return total_cost[n - 1]
