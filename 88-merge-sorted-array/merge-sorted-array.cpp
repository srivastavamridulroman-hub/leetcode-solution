class Solution {
public:
    void merge(vector<int>& a, int n, vector<int>& b, int m) {
        
        vector<int> res(n + m);

        int i = 0, j = 0, id = 0;

        while(i < n && j < m){
            if(a[i] <= b[j]){
                res[id++] = a[i++];
            
            }
            else{
                res[id++] = b[j++];
               
            }
        }

        while(j < m){
            res[id++] = b[j++];
        }

        while(i < n){
            res[id++] = a[i++];
        }

        
        for(int k = 0; k < n + m; k++){
            a[k] = res[k];
        }
    }
};