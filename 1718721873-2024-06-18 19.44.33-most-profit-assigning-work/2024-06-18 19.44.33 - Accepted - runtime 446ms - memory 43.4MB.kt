class Solution {
    fun maxProfitAssignment(difficulty: IntArray, profit: IntArray, worker: IntArray): Int {
        var difficultyProfit = HashMap<Int, Int>()
        for (i in 0..difficulty.lastIndex) {
            difficultyProfit[difficulty[i]] = max(difficultyProfit[difficulty[i]] ?: 0, profit[i]);
        }
        difficulty.sort();
        for (i in 1..difficulty.lastIndex) {
            var cur = difficultyProfit[difficulty[i]] ?: 0
            var prev = difficultyProfit[difficulty[i-1]] ?: 0
            difficultyProfit[difficulty[i]] = max(cur, prev)
        }

        var maxProfit = 0
        for (w in worker) {
            var difficultyIdx = difficulty.binarySearch(w);
            var diff = 0
            if (difficultyIdx < 0) {
                difficultyIdx = -(difficultyIdx + 2)
                if (difficultyIdx < 0) continue
            }

            diff = difficulty[difficultyIdx]
            maxProfit += difficultyProfit[diff] ?: 0
        }

        return maxProfit
    }
}