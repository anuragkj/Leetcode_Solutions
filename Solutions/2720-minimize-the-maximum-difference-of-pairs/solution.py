# TLE Error class Solution {
# public:

#     //DP solution (Giving Memory Limit Exceed)
#      int solve(int i,vector<int>& nums, int p, vector<vector<int>> &dp){
#      if(p==0)return 0;
#          if(i>=nums.size()-1)return 1e9;
#          if(dp[i][p]!=-1)
#          return dp[i][p];

#         int liya=0,nhiliya=0;
#         if(i+1<nums.size())
#          liya = max(abs(nums[i]-nums[i+1]),solve(i+2,nums,p-1,dp));
            
    
#          nhiliya = solve(i+1,nums,p,dp);

#              return dp[i][p] = min(liya,nhiliya);

#          }
#          int minimizeMax(vector<int>& nums, int p) {
#              sort(nums.begin(),nums.end());
       
#             int n = nums.size();
#             vector<vector<int>> dp(n,vector<int>(p+1,-1));

#             return solve(0,nums,p,dp);
#          }


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left       
