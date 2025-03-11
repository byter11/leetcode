class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<string> ans;
        for(int i=0; i<26; i++) {
            int count = 0;
            for(int j=0; j<words.size(); j++) {
                int local_count = 0;
                for(char &c: words[j]) {
                    if(c-'a' == i) local_count++;
                }

                if (local_count < count || j == 0) count = local_count;
            }

            for(int k=0; k<count; k++) ans.push_back(string() + char(i+'a'));
        }

        return ans;
    }
};