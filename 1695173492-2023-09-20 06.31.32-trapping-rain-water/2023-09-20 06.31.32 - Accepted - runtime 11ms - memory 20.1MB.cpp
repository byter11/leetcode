class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int trapped = 0, i = 0, j = n-1;
        int begin = height[i], end = height[j];
        while(i <= j) {
            if (height[i] >= begin)
                begin = height[i++];
            else if(begin <= end){
                trapped += begin - height[i++];
            }
            else if (height[j] >= end)
                end = height[j--];
            else if(end <= begin) {
                trapped += end - height[j--];
            }
        }
        return trapped;
    }
};