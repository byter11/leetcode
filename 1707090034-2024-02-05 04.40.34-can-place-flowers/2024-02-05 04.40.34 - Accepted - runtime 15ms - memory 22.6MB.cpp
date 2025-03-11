class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(flowerbed.size()==1) return n ==0 || flowerbed[0] == 0;
        int b = 0;
        if(flowerbed.size() >1 && flowerbed[0] == 0 && flowerbed[1] == 0) { flowerbed[0] = 1; b++; }
        
        for(int i=1;i<flowerbed.size()-1;i++){
            if(flowerbed[i-1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0) { flowerbed[i]=1; b++; }
    }
    
    int k=flowerbed.size()-1;
    if(k!=0 && flowerbed[k]==0 && flowerbed[k-1]==0) b++;
        
        return b>=n;
}
};