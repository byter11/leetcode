class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> freq;
        for(int &n: nums) freq[n]++;
        
        vector<int> s = mergeSort(nums, [&freq](const int& a, const int& b) {
            if(freq[a] == freq[b]) return a > b;
            return freq[a] < freq[b];
        });

        return s;
    }

    vector<int> mergeSort(vector<int> &nums, auto lambda) {
        if(nums.size() == 1) return nums;

        vector<int> l, r;
        for(int i=0; i<nums.size(); i++) {
            if(i >= nums.size()/2) r.push_back(nums[i]);
            else l.push_back(nums[i]);
        }

        vector<int> mergedL = mergeSort(l, lambda);
        vector<int> mergedR = mergeSort(r, lambda);
        vector<int> merged;
        int i=0, j=0;

        while(i<mergedL.size() && j<mergedR.size()) {
            if(lambda(mergedL[i], mergedR[j])) merged.push_back(mergedL[i++]);
            else merged.push_back(mergedR[j++]);
        }
        for(i; i<mergedL.size(); i++) merged.push_back(mergedL[i]);
        for(j; j<mergedR.size(); j++) merged.push_back(mergedR[j]);

        return merged;
    }
};