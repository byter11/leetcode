class Solution {
    fun minDays(bloomDay: IntArray, m: Int, k: Int): Int {
        if (bloomDay.size / m < k) return -1;
        var minDays = bloomDay.minOrNull() ?: 0
        var maxDays = bloomDay.maxOrNull() ?: 0

        var answer = -1

        while(minDays <= maxDays) {
            // println("${minDays} ${maxDays}")
            var mid: Int = (minDays + maxDays) / 2
            if(canMakeBouquets(bloomDay, m, k, mid)) {
                answer = mid
                maxDays = mid - 1
            }
            else {
                minDays = mid + 1
            }
        }

        return answer
    }

    fun canMakeBouquets(bloomDay: IntArray, m: Int, k: Int, day: Int): Boolean {
        var bouquets = 0
        var current = 0
        for(d in bloomDay) {
            if(d <= day) 
                current +=1
            else
                current = 0
            if(current == k) {
                current = 0
                bouquets++
            }
        }

        return bouquets >= m
    }
}

// [5, 3, 3, 4, 3, 3, 100]