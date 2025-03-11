class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
       int curr_color = image[sr][sc];
       if(curr_color == color) return image;
       image[sr][sc] = color;

       if(sr-1 >= 0 && image[sr-1][sc] == curr_color) floodFill(image, sr-1, sc, color); 
       if(sr+1 < image.size() && image[sr+1][sc] == curr_color) floodFill(image, sr+1, sc, color); 
       if(sc-1 < image[sr].size() && image[sr][sc-1] == curr_color) floodFill(image, sr, sc-1, color); 
       if(sc+1 >= 0 && image[sr][sc+1] == curr_color) floodFill(image, sr, sc+1, color); 

       return image;
    }
};