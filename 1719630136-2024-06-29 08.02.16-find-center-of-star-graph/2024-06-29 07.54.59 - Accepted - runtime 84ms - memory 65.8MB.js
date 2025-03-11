
/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    const obj = {}
    for(let edge of edges) {
        obj[edge[0]] = (obj[edge[0]] || 0) + 1
        obj[edge[1]] = (obj[edge[1]] || 0) + 1

        if(obj[edge[0]] > 1) return edge[0];
        if(obj[edge[1]] > 1) return edge[1];
    }

    return 0;
};
