class Solution {
public:
    int kthGrammar(int n, int k) {
        int cur = 0;
        int j = 0;
        int ans = cur;

        for(int i=0; i<n-1; i++) {
            j += pow(2,i);
        }
        j += k-1;

        while(--n) {

            // if right child, swap digit
            if(j%2 == 0) cur = !cur;

            cout << j << ' ' << cur << '\n';


            j = (j-1)/2;    // move to parent node
        }

        if(cur == 0) return 0;
        if(j%2 == 0) return 1;

        return 1;
    }
};

                    //          0
                    //      0       1
                    //    0   1   1   0
                    //   0 1 1 0 1 0 0  1