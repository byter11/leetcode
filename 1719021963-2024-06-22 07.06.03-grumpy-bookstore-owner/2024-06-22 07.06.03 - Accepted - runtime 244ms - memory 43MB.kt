class Solution {
    fun maxSatisfied(customers: IntArray, grumpy: IntArray, minutes: Int): Int {
        var maxProfit = customers.slice(0..<minutes).sum()
        for(i in minutes..<customers.size) {
            if (grumpy[i] == 0) maxProfit += customers[i]
        }

        // println(maxProfit)
        var left = 0
        var right = minutes
        var lastProfit = maxProfit
        for(i in 1..customers.size - minutes) {
            var lost = if (grumpy[i-1] == 1) customers[i-1] else 0
            var gain = if (grumpy[i+minutes-1] == 0) 0 else customers[i+minutes-1]

            lastProfit = lastProfit - lost + gain
            maxProfit = max(maxProfit, lastProfit)
            // println("${customers[i-1]}:${lost} ${customers[i+minutes-1]}:${gain} ${maxProfit}")
        }
        
        return maxProfit
    }
}

// [1,0,1,2,1,1,7,5]
// [0,1,0,1,0,1,0,1]

// [1,1,1,1,0,1,0,1]
// [1,0,1,2,0,1,0,5] = 10

// [0 1,1,1,0,1,0,1]
// [0,0,1,2,0,1,0,5] = 9


// 1 + 1 + 1 + 1 + 1 + 7 + 5 + 5 + 5 + 5 = 32
// 
