class Solution {
    fun threeConsecutiveOdds(arr: IntArray): Boolean {
        var i = 0
        while(i < arr.size) {
            while(i < arr.size && arr[i] % 2 == 0) {
                i++
            }
            var j = i
            while(j < arr.size && arr[j] % 2 == 1) {
                j++
                if(j - i >= 3) return true
            }

            i = j
        }

        return false
    }
}