class Solution {
public:

    int bits(int num) {
        int count = 0;
        for(int i = 0; i<32; i++) {
            if(num&1) count++;
            num >>= 1;
        }

        return count;
    }

    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [this](const int &a, const int &b) {
            int bits_a = bits(a), bits_b = bits(b);
            if(bits_a == bits_b) return a < b;
            return bits_a < bits_b;
        });

        return arr;
    }
};