"""
link: https://leetcode.com/problems/peak-index-in-a-mountain-array/

problem: Let's call an array arr a mountain if the following properties hold:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[-1]

Given an integer array arr that is guaranteed to be a mountain, return any i
such that arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[-1].

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Constraints:
3 <= arr.length <= 10^4
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.
 
Follow up: Finding the O(n) is straightforward, could you find an O(log(n))
solution?
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i


# follow up:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle - 1] < arr[middle] and arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle - 1] < arr[middle] < arr[middle + 1]:
                left = middle
            else:
                right = middle
