# #pseucode from group:
#     # for i from 2 to n-1:
#     # dp[i] = max(dp[i-1], nums[i] + dp[i-2] if i > 1 else 0)
#     # result = []
#     # i = n - 1
#     # while i >= 0:
#     # if (i == 0 or dp[i] != dp[i-1]) AND dp[i] >= 0:
#     # result.append(nums[i])
#     # i -= 2
#     # else:
#     # i -= 1
#     # return result[::-1]


def max_independent_set(nums): 
    n = len(nums)
    
    if n == 0:
        return []
    
    if all(num < 0 for num in nums):
        return []
    
    dp = [0] * n # initializes array of size n
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    
    result = []
    i = n - 1
    while(i >= 0):
        # if (i == 0 or (i > 0 and dp[i] != dp[i - 1] and dp[i - 1] >= 0)):
        if((i == 0 or dp[i] != dp[i - 1]) and dp[i] >= 0):
            result.append(nums[i])
            i -= 2
        else:
            i -= 1
    
    return result[::-1]

# Test cases
# input = [7, 2, 5, 8, 6]  # [7, 5, 6]
# input2 = [-1, -1, 0]  # [0]
# input3 = [-1, -1, -10, -34]  # []
# print(max_independent_set(input))
# print(max_independent_set(input2))
# print(max_independent_set(input3))
