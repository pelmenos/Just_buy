from typing import List


# def maxProfit(nums: List[int]) -> int:
#     index = 0
#     count = 0
#     while index + 1 < len(nums):
#         if nums[index] == 0:
#             if nums[count] == 0:
#                 return False
#             count += 1
#             index = count
#         index += nums[index]
#
#     return True
# def maxProfit(nums: List[int]) -> int:
#     index = 0
#     count = 0
#     while index + 1 < len(nums):
#         if index + 1 != len(nums) and nums[index] == 0:
#             count += 1
#             index = count
#         if count + 1 == len(nums):
#             return False
#         index += nums[index]
#     return True


def solution(nums: List[int]) -> int:
    goal = len(nums)-1

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False

nums = [2,3,1,1,4]

print(solution(nums))

