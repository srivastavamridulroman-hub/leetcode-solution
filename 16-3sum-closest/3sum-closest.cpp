class Solution {

public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        
        int result=0;
        int min_diff = INT_MAX;
        for(int i=0;i<n-2;i++)
        {
            int left = i+1;
            int right = n-1;
            while(left<right)
            {
                int sum = nums[i]+nums[left]+nums[right];
                int diff = abs(sum-target);
                if(diff<min_diff)
                {
                    min_diff=diff;
                    result=sum;
                }
                if(sum<target) 
                left++;
                else if (sum>target)
                 right--;
                else {
                    
                    return sum;
                }
            }
        }
        return result;
    }
};
        
