class Solution:
    def climbStairs(self, n: int) -> int:
        # constraint = 1 <= n <= 45
        memo = {}

        def f(currentStep):
            if currentStep == n:
                return 1
            if currentStep > n:
                return 0
            if currentStep in memo:
                return memo[currentStep]

            ways = f(currentStep + 1) + f(currentStep + 2)
            memo[currentStep] = ways
            return ways

        return f(0)
