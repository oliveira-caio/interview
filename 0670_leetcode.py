class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        max_index = len(digits) - 1
        x = y = 0
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] > digits[max_index]:
                max_index = i
            elif digits[i] < digits[max_index]:
                x, y = i, max_index
        digits[x], digits[y] = digits[y], digits[x]
        return int(''.join((str(x) for x in digits)))
