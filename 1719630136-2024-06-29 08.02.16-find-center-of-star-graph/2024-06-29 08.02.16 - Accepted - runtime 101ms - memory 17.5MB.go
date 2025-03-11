func findCenter(edges [][]int) int {
    m := make(map[int]int)
    for _, e := range edges {
        m[e[0]]+= 1
        m[e[1]]+= 1
        if m[e[0]]>1 { return e[0] }
        if m[e[1]]>1 { return e[1] }
    }
    return 0
}