class Solution {
public:
    int removeDuplicates(vector<int>& arr) {
        int n = arr.size();
        if(n == 0) return 0;

        int i = 0, j=1;

        while(j<n)
        {
            if(arr[j] != arr[i]) {
                i++;
                arr[i] = arr[j];
            
            }
            j++;
        }

        return i+1;
    }
};