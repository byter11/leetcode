class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        vector<string> answer(n);

        unordered_map<int, int> places;
        for(int i=0; i<n; i++) {
            places[score[i]] = i;
        }

        sort(score.begin(), score.end(), std::greater());
        
        for(int i=0; i<n; i++) {
            int place = places[score[i]];
            answer[place] = getRank(i);
        }

        return answer;
    }

    string getRank(int place) {
        if(place == 0) return "Gold Medal";
        if(place == 1) return "Silver Medal";
        if(place == 2) return "Bronze Medal";
        return to_string(place + 1);
    }
};