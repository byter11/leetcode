func partitionString(s string) int {
    substrings := 1
    seen := make(map[rune]struct{})
    
    for _, c := range s {
        if _, ok := seen[c]; ok {
            substrings++
            seen = make(map[rune]struct{})
        }
        seen[c] = struct{}{}
    }

    return substrings
}

// hdklqkcssgxlvehva
// hdklq cs gx ve  a
//      k  s  l  hv