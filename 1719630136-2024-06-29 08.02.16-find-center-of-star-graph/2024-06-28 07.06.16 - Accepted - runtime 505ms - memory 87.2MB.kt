class Solution {
    fun findCenter(edges: Array<IntArray>): Int {
        var nEdges = HashMap<Int, Int>();

        for(edge in edges) {
            var edgeIn = edge.get(0)
            var edgeOut = edge.get(1) 
            nEdges[edgeIn] = nEdges.getOrElse(edgeIn) { 0 } + 1
            nEdges[edgeOut] = nEdges.getOrElse(edgeOut) { 0 } + 1
        }

        return nEdges.maxBy { it.value } ?.key ?: 0
    }
}