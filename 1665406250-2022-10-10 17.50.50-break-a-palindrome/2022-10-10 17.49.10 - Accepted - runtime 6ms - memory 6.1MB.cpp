class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        if(n == 1) return "";
        
        int i=0;
        while(i < n && palindrome[i] == 'a') {
          i++;
          if(n&1 && i == n/2) i++;
        } 
        
        if(i == n) palindrome[n-1] = palindrome[n-1]+1;
        else palindrome[i] = 'a';
        
        return palindrome;
    }
};