class Solution {
public:
    int removeDuplicates(vector<int>& arr) {
        int n = arr.size();
        

        int i = 0;
        int j = 1;
        int res = 1;

        while(j < n) {
            if(arr[j] == arr[i]) {
                j++;
            } else {
                arr[i+1] = arr[j]; // write first
                i++;               // then move i
                j++;
                res++;
            }
        }

        return res;
    }
};