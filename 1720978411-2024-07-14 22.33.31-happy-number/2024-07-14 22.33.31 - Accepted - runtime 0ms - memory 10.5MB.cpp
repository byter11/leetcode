class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while(n != 1) {
            if (seen.contains(n)) {
                return false;
            }
            seen.insert(n);
            n = sumsquare(n);
        }

        return true;
    }

    int sumsquare(int n) {
        int result = 0;
        string s = to_string(n);
        for(char &c: s) {
            result += (int(c)-48) * (int(c)-48);
        }

        return result;
    }
};