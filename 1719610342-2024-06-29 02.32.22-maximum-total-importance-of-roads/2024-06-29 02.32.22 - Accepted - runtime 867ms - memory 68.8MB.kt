class Solution {
    fun maximumImportance(n: Int, roads: Array<IntArray>): Long {
        var cityMap = HashMap<Int, Int>();
        for(road in roads) {
            cityMap[road[0]] = cityMap.getOrElse(road[0]) { 0 } + 1
            cityMap[road[1]] = cityMap.getOrElse(road[1]) { 0 } + 1
        }

        var cityOrder = cityMap.keys.sortedByDescending { cityMap[it] }
        for(i in cityOrder.indices) {
            cityMap[cityOrder[i]] = n - i
        }

        return roads.map { ((cityMap[it[0]]?:0) + (cityMap[it[1]]?:0)).toLong() }.sum()
    }
}