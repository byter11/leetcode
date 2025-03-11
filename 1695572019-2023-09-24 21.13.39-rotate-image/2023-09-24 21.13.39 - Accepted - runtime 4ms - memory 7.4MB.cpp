class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i=0; i<n/2; i++) {
            for(int j=i; j<n-i-1; j++) {
                swap(matrix[i][j], matrix[j][n-i-1]);
                swap(matrix[i][j], matrix[n-j-1][i]);
                swap(matrix[n-j-1][i], matrix[n-i-1][n-j-1]);
            }
        }
    }
};

// 7 4 1
// 6 5 2
// 3 8 9

// 15 13  2  5
// 14  4  8  1
// 10  3  6  9
// 11  7 12 16

//  5  1  9 11 17
//  2  4  8 10 18
// 13  3  6  7 19
// 15 14 12 16 20
// 21 22 23 24 25
