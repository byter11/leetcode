class Solution {
    vector<string> result;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordMap;
        for(int i=0; i<wordDict.size(); i++) wordMap.insert(wordDict[i]);

        return breakWords(s, 0, wordMap, "");
    }

    vector<string> breakWords(string s, int i, unordered_set<string>& wordDict, string word) {
        vector<string> res;

        // cout << word << " ->" << "(" << i << ") ";

        vector<string> next = nextWords(s, wordDict, i);
        
        map<string, vector<string>> m;

        for(int j=0; j<next.size(); j++) {
            if(i + next[j].size() == s.size()) {
                res.push_back(next[j]);
                break;
            }

            for (string s: breakWords(s, i + next[j].size(), wordDict, next[j])) {
                m[next[j]].push_back(s);
            }
        }

        for(auto p: m) {
            for(string s: p.second) {
                res.push_back(p.first + " " + s);
            }
        }

        return res;
    }

    vector<string> nextWords(string s, unordered_set<string>& wordDict, int i) {
        vector<string> words;

        for(int j = 1; j <= s.size() - i; j++) {
            // cout << s.substr(i, j) << ':';
            if(wordDict.contains(s.substr(i, j))) {
                words.push_back(s.substr(i, j));
            }
        }

        // cout << '\t';
        // for(string s: words) cout << s << ' ';
        // cout << '\n';


        return words;
    }
};