# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the
# line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms
# a container, such that the container contains the most water.


class Solution():
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                temp_area = (j-i)*height[i]
                i += 1
            else:
                temp_area = (j-i)*height[j]
                j -= 1

            if max_area < temp_area:
                max_area = temp_area

        return max_area

    def maxArea2(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                temp_area = abs(i-j)*min(height[i], height[j])
                if max_area < temp_area:
                    max_area = temp_area

        return max_area


sol = Solution()
print(sol.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
