class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffix = [1]
        suffix = [1]
        for i in range(1, len(nums)):
            preffix.append(nums[i - 1] * preffix[i - 1])
            suffix.append(nums[-i] * suffix[i - 1])
        return [preffix[i] * suffix[-i-1] for i in range(len(nums))]


# follow up (the idea is to create the preffix and the suffix in two loops):
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]; temp = 1
        for i in range(1, len(nums)):
            ans.append(nums[i - 1] * ans[i - 1])
        for i in range(2, len(nums) + 1, 1):
            temp *= nums[-i + 1]
            ans[-i] *= temp
        return ans
