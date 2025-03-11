class Solution {
public:
    int hIndex(vector<int>& citations) {
        if(citations.size() == 1) return min(1, citations[0]);

        sort(citations.begin(), citations.end(), greater<int>());
        int minDiff = 0;
        for(int i=1; i<citations.size(); i++) {
            int diff = min(citations[i], i+1);
            if(diff >= min(citations[minDiff], minDiff + 1)) minDiff = i;
            else break;
        }

        return min(citations[minDiff], minDiff+1);
    }
};

// 6 5 3 1 0
// (6,1), (5, 2), (3, 3), (1, 4), (0, 5)
// 1 2 3 1 0

// 10 10 7 1 1
// (10, 1) (10, 2) (7, 3) (1, 4) (1, 5)
// 9 8 4 3 4

// 1 4 times not better than 7 3 times