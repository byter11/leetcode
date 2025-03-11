func maxDepth(s string) int {
    depth := 0
    maxDepth := 0
    for _, c := range s {
        if c == '(' {
            depth += 1
            if depth > maxDepth {
                maxDepth = depth
            }
        }
        if c == ')' {
            depth -= 1
        }
    }

    return maxDepth
}