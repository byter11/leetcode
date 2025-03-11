class Solution {
public:
    bool isPerm(string s, unordered_map<string, int> words, int wlen) {
        for(int i=0; i<=s.size() - wlen; i += wlen) {
            string substr = s.substr(i, wlen);
            if(!words[substr]) {
                return false;
            }
            else {
                words[substr]--;
            }
        }
        return true;
    }

    vector<int> findSubstring(string s, vector<string>& words) {
        int n = s.size();
        int w = words.size();
        int wlen = words[0].size();
        int readlen = w * wlen;
        unordered_map<string, int> m;
        vector<int> res;
        
        for(string w: words) {
            m[w]++;
        }
        int i = 0;
        while(i <= n - readlen) {
            string substr = s.substr(i, readlen);
            if(isPerm(substr, m, wlen)) {
                res.push_back(i);
            }
            i++;
        }

        return res;
    }
};