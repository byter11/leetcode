class Solution {
public:
    int getWinner(vector<int>& arr, int k) {

        if(k >= arr.size()) return *max_element(arr.begin(), arr.end());

        int i1=0, i2=1;
        map<int,int> wins;

        while(i2 < arr.size()) {
            int p1 = arr[i1], p2 = arr[i2];

            if(p1 > p2) {
                arr.push_back(p2);
                wins[p1]++;
                if(wins[p1] == k) return p1;
                i2++;
            } else {
                arr.push_back(p1);
                wins[p2]++;
                if(wins[p2] == k) return p2;
                i1 = i2;
                i2++;
            }
        }

        return -1;
    }
};