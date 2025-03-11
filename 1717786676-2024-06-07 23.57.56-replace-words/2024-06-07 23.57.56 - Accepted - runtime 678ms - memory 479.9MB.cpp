class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        unordered_set<string> d;
        for(string &s: dictionary) d.insert(s);

        istringstream iss(sentence);
        string s;        
        string ans = "";

        while(getline(iss, s, ' ')) {
            bool found = 0;
            for(int i=0; i<s.size(); i++) {
                if(d.contains(s.substr(0, i+1))) {
                    if(ans != "") ans += " ";
                    ans += s.substr(0, i+1);
                    found = 1;
                    break;
                }
            }

            if(!found) {
                if(ans != "") ans += " ";
                ans += s;
            }
        }

        return ans;
    }
};