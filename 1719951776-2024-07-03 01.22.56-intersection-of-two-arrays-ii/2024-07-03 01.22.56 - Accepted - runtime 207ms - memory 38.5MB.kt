class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        var map = HashMap<Int, IntArray>()

        for (num in nums1) {
            map.getOrPut(num) { intArrayOf(0,0) }[0]++
        }

        for (num in nums2) {
            map.getOrPut(num) { intArrayOf(0,0) }[1]++
        }

        var ans = ArrayList<Int>()
        for((k, v) in map) {
            for(i in 0..<v.min()) ans.add(k)
        }

        return ans.toIntArray()
    }
}