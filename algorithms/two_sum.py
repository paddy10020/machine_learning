class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        result = []
        list_len = len(nums)
        new_list = sorted(nums)

        for i in range(list_len):
            for j in range(list_len - i -1):
                a = new_list[i]
                b = new_list[list_len - j - 1]
                sum = a + b
                if sum < target:
                    break
                if sum == target:
                    if a != b:
                        result.append(nums.index(a))
                        result.append(nums.index(b))
                        break
                    if a == b:
                        result.append(nums.index(a))
                        result.append(nums.index(a, nums.index(a) + 1))
                        break
                else:
                    continue
        return result


a = Solution()
b = a.twoSum([2, 5, 5, 11], 10)
print(b)
