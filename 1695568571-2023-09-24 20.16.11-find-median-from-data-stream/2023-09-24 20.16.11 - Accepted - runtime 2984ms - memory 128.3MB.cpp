class MedianFinder {
    vector<int> heap;

public:
    multiset<int> arr;

    MedianFinder() {
    }
    
    void addNum(int num) {
        arr.insert(num);
    }

    
    double findMedian() {
        int n = arr.size();
        auto it = arr.begin();
        if(n == 1) return *it;
        advance(it, n/2 - 1);
        if(n%2 == 0) return ((double)*it + *(++it))/2;
        return *(++it);
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

 // 1               1
 // 1 2             1 2
 // 1 2 3           2
 // 1 2 3 4         2 3
 // 1 2 3 4 5       3
 // 1 2 3 4 5 6     3 4
 // 1 2 3 4 5 6 7   4