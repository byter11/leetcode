class Solution {
public:
    int binarySearch(vector<int>& arr, int x) {
      int left=0, right=arr.size()-1, mid=0;
      while (left <= right) {
        mid = left + (right - left) / 2;
        if (arr[mid] == x)
          return mid;
        else if (arr[mid] < x)
          left = mid + 1;
        else 
          right = mid - 1;
        }
        return mid-1;   
    }
    
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        vector<int> res;
        if(n == 1)
            return arr;
        int i = max(0, binarySearch(arr, x));
        int l=i, r=i+1;
        if(arr[i] == x) {
            res.push_back(x);
            k--; l--;
        }
        
        
        for(int i=0; i<k; i++) {
            if(l<0 || (r<n && (abs(arr[l] - x) > abs(arr[r] - x)))) {
                // cout << arr[r] << " ";
                res.push_back(arr[r++]);
            }
            else {
                // cout << arr[l] << " ";
                res. push_back(arr[l--]);
            }
        }
        // cout << '\n';
        sort(res.begin(), res.end());
        return res;
    }
};

// 1 4 5 6 12 12 16 17

