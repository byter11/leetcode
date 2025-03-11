class SeatManager {
public:
    set<int> seats;

    SeatManager(int n) {
        seats = set<int>();
        for(int i=1; i<=n; i++) {
            seats.insert(i);
        }    
    }
    
    int reserve() {
        auto seat = seats.begin();
        int s = *seat;
        seats.erase(seat);
        return s;
    }
    
    void unreserve(int seatNumber) {
        auto it = seats.lower_bound(seatNumber);
        seats.insert(it, seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */