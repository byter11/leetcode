class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size();
        string ans = "";
        if(numRows == 1) return s;

        for(int i=0; i<numRows; i++) {
            int down = 2*(numRows-i-2) + 1;
            int up = 2*(i-1) + 1;

            cout << up << ':' << down << ' ';
            int j = i;
            int col = 0;
            while(j < n) {
                ans += s[j];
                col++;

                if(up == -1)  j += down + 1;
                else if(down == -1)  j += up + 1;
                else if(col%2 == 0) j += up + 1;
                else j += down + 1;
            }
        }

        return ans;
    }
};