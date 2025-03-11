class Solution {
    fun minDifference(nums: IntArray): Int {
        if(nums.size <= 4) return 0;

        nums.sort();
        var ans = Int.MAX_VALUE

        var j = nums.size-4
        for(i in 0..3) {
            ans = min(ans, nums[j] - nums[i])
            j++
        }

        return ans
    }
}


// 0 1 5 10 14
// 

// 0 0 4 4 4 0 2 1 -> 
// 5 4 3 2 1 -> 2 2 2 2

// 0 1 1 4 6 6 6
// 1 4 6 6 6