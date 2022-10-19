class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        min_diff = math.inf

        for i in range(len(nums)-2):
            left = i + 1
            right = length - 1
            while(left < right):
                current_sum = nums[i] + nums[left] + nums[right]
                diff = target - current_sum

                if abs(diff) < abs(min_diff) or (abs(diff) == abs(min_diff) and diff > min_diff):
                    min_diff = diff  # save the closest and the biggest difference

                if diff == 0: break
                elif diff > 0: left += 1
                else: right -= 1

        return target - min_diff
