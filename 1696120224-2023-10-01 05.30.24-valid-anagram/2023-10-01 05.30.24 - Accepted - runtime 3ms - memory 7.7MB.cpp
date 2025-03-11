class Solution {
public:
    bool isAnagram(string s, string t) {
        int used = 0;
        unordered_map<char, int> m;
        for(char c: s) m[c]++;

        for(char c: t) {
            if(!(m[c]--)) return false;
            used++;
        }

        return used == s.size() ? true : false;
    }
};