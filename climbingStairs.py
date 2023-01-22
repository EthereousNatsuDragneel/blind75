#logic is almost the same as fibonacci series
class Solution(object):
    def climbStairs(self, n):
		steps = [1, 2]
		if n>2:
			i = 3
			while i<=n:
				steps.append(steps[i-1] + steps[i-2])
				i=i+1
		return steps[n]