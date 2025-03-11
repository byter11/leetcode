class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        map<char, int> m;
        for(char c: chars) m[c]++;

        int ans = 0;
        for(string word: words) {
            if(isGood(word, m)) ans += word.size();
        }

        return ans;
    }

    bool isGood(string word, map<char, int> m) {
        for(char c: word) {
            if(m[c] == 0) return false;
            m[c]--;
        }
        return true;
    }
};