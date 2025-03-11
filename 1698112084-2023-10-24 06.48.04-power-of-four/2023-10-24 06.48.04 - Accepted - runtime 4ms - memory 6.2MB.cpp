class Solution {
public:
    bool isPowerOfFour(int n) {
        while(n > 0 && n % 2 == 0) {
            n >>= 1;
            if(n & 1) return false;
            n >>= 1;
        }
        if(n == 1) return true;

        return false;
    }
};
