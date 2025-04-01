class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Get the number of questions
        n = len(questions)

        # Initialize DP array where dp[i] represents the maximum points
        # we can earn starting from the ith question
        dp = [0] * n

        # Base case: For the last question, we just take its points value
        dp[n-1] = questions[n-1][0]

        # Fill the dp array from right to left (bottom-up approach)
        for i in range(n-2,-1,-1):
            points,brainpower = questions[i]

            # Option 1: Solve the current question
            # We add the points of current question and the maximum points we can get
            # after skipping the next 'brainpower' questions
            next_available_index = min(i + brainpower + 1 , n)
            solve_points = points + (dp[next_available_index] if next_available_index < n else 0)

            # Option 2: Skip the current question
            # We take the maximum points we can get starting from the next question
            skip_points = dp[i+1]

            # The optimal strategy is to take the maximum of the two options
            dp[i] = max(solve_points , skip_points)

        # dp[0] now contains the maximum points possible starting from the first question
        return dp[0]
