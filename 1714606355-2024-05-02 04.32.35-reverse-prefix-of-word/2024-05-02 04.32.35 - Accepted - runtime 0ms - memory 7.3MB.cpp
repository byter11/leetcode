class Solution {
public:
    string reversePrefix(string word, char ch) {
        int n = word.size();
        int k = n;
        for(int i=0; i<n; i++) {
            if(word[i] == ch) {
                k = i;
                break;
            }
        }

        if(k == n) return word;

        for(int i=0; i<=k/2; i++) {
            swap(word[i], word[k-i]);
        }

        return word;
    }
};