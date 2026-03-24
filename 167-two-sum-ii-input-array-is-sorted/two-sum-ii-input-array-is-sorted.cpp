class Solution {
public:
    vector<int> twoSum(vector<int>& num, int target) {
        //mridul
        int n=num.size();
        
        int left = 0;
        int right = n - 1;

        while (left < right) {
            int sum = num[left] + num[right];

            if (sum == target) {
                return {left + 1, right + 1};  // convert to 1-based index
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }

        return {};
    }
};