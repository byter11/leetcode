class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int i = 0, j = n-1;

        while(i < j) {
            char a = to_alpha(s[i]);
            char b = to_alpha(s[j]);
            if(!a) i++;
            else if(!b) j--;
            else if(a != b) return false;
            else { i++; j--; }
        }
        return true;
    }

    char to_alpha(char c) {
        if((c>='a' && c<='z') || (c>='0' && c<='9')) 
            return c;
        if(c>='A' && c <= 'Z') 
            return c + ('a'-'A');
        return 0;
    }
};