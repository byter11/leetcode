class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        map<int, int> converted;
        for(int &n: nums) converted[n] = convert(n, mapping);
        // for(int &n: nums) cout << n << ": " << converted[n] << '\n';
        
        sort(nums.begin(), nums.end(), [&converted](const int& a, const int& b) {
            if(converted[a] == converted[b]) return false;
            return converted[a] < converted[b];
        });

        return nums;
    }

    int convert(int num, vector<int>& mapping) {
        if(num == 0) return mapping[0];

        int converted = 0;
        int unit = 1;
        while(num > 0) {
            converted = mapping[num%10]*unit + converted;
            num /= 10;
            unit *= 10;
        }

        return converted;
    }
};