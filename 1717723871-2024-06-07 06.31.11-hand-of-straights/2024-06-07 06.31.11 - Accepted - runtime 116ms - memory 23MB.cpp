class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        sort(hand.begin(), hand.end());

        int groups = 0;
        while(true) {
            int group = 0;
            int last = -1;
            for(int j=0; j<hand.size(); j++) {
                // cout << hand[j] << ' ' << last << '\n';
                if((hand[j] != -1 && last == -1) || hand[j] - 1 == last) {
                    last = hand[j];
                    // cout << last << ' ';
                    hand[j] = -1;
                    group++;
                }

                if(group == groupSize) {
                    groups++;
                    break;
                }
            }

            if(group != groupSize) break;
        }

        for(int i=0; i<hand.size(); i++) { 
            // cout << hand[i] << ' ';
            if(hand[i] != -1) return false;}

        cout << '\n' << groups;
        return groups > 0 && hand.size() / groups == groupSize && hand.size() % groups == 0;
    }
};