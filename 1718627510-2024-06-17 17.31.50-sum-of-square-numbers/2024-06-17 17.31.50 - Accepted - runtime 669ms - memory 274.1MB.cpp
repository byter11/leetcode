class Solution {
public:
    bool judgeSquareSum(int c) {
        unordered_set<int> powers;
        for(int i=0; i<=min(c, 46340); i++) {
            powers.insert(i*i);
        }

        for(int i=0; i<=min(c, 46340); i++) {
            if(powers.contains(c - (i*i))) return true;
        }

        return false;
    }
};