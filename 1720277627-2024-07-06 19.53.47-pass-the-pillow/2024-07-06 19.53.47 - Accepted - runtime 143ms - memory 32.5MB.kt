class Solution {
    fun passThePillow(n: Int, time: Int): Int {
        var dir = -1
        var ans = 1
        for(i in 1..time) {
            if(ans == 1 || ans%n == 0) dir *= -1
            ans += dir
        }

        return ans
    }
}

// 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
//     *