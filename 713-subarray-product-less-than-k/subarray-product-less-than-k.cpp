class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        
        if(k <= 1) return 0;  // important edge case
        
        int left = 0;
        int product = 1;
        int count = 0;
        
        for(int right = 0; right < nums.size(); right++) {
            
            product *= nums[right];  // expand window
            
            // shrink window if product >= k
            while(product >= k) {
                product /= nums[left];
                left++;
            }
            
            // count subarrays ending at right
            count += (right - left + 1);
        }
        
        return count;
    }
};