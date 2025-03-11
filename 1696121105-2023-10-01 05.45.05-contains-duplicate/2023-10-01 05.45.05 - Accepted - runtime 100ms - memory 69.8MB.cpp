class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(int &num: nums) {
            if(s.contains(num)) return true;
            s.insert(num);
        }

        return false;
    }
};