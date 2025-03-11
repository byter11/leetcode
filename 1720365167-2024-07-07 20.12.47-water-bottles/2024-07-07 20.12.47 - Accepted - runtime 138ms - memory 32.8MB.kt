class Solution {
    fun numWaterBottles(numBottles: Int, numExchange: Int): Int {
        var drink = 0
        var full = numBottles
        var empty = 0

        while(full + empty >= numExchange) {
            drink += full
            var total = full + empty
            full = total / numExchange
            empty = total % numExchange
        }

        return drink + full
    }
}