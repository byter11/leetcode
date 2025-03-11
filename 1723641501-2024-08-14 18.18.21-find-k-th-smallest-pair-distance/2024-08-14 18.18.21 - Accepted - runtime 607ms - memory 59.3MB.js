/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestDistancePair = function(nums, k) {
    const n = nums.length;
    const mx = Math.max(...nums);
    const mn = Math.min(...nums);
    
    const counts = Array(mx-mn + 1).fill(0);
    for(let i=0; i<n; i++) {
        for(let j=i+1; j<n; j++) {
            counts[Math.abs(nums[j] - nums[i])] += 1;
        }
    }

    for(let i=0; i<mx-mn + 1; i++) {
        k -= counts[i];
        if(k <= 0) return i;
    }

    return -1;
};