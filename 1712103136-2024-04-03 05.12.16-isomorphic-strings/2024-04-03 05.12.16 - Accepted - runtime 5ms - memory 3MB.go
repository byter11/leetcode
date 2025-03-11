func isIsomorphic(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    ref := make(map[byte]byte)
    used := make(map[byte]int)

    for i := 0; i<len(s); i++ {
        if _, ok := ref[s[i]]; !ok {
            if _, ok := used[t[i]]; ok {
                return false
            }
            ref[s[i]] = t[i]
            used[t[i]] = 1
        } else if ref[s[i]] != t[i] {
            return false
        }
    }

    return true
}