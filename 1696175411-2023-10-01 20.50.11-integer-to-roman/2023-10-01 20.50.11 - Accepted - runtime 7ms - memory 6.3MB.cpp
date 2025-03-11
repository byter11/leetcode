class Solution {
    const string p[5] = {"I", "X", "C", "M"};
    const string b[5] = {"V", "L", "D"};
public:
    string intToRoman(int num) {
        int i = 1;
        int pow = 10;
        string ans;
        while(num) {
            int last = num%(pow);
            num /= pow;
            ans = numToRoman(last, i-1) + ans;
            i++;
        }

        return ans;
    }

    string numToRoman(int num, int place) {
        if(num == 0) return "";

        string s = "";
        if(num == 5)
            return b[place];
        if(num == 4)
            return p[place] + b[place];
        if(num == 9)
            return p[place] + p[place+1];
        
        if(num > 5) {
            num -= 5;
            s += b[place];
        }

        for(int i=0; i<num; i++)
            s += p[place];

        return s;
    }
};