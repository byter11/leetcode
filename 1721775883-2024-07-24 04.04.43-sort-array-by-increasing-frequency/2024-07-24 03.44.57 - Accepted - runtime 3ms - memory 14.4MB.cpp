class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> freq;
        for(int &n: nums) freq[n]++;

        sort(nums.begin(), nums.end(), [&freq](const int& a, const int& b) {
            if(freq[a] == freq[b]) return a > b;
            return freq[b] > freq[a];
        });

        return nums;
    }
};