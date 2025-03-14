class Solution {
public:
    int tribonacci(int n) {
        int a = 0, b = 1, c = 1;
        if(n == 0) return a;
        if(n == 1) return b;
        if(n == 2) return c;

        int d = 2;
        for(int i=3; i<=n; i++) {
            d = a + b + c;
            a = b;
            b = c;
            c = d;
        }

        return d;
    }
};