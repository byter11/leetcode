func makeGood(s string) string {
    i := 0
    for i < len(s) - 1 {
        if s[i] != s[i+1] && unicode.ToUpper(rune(s[i])) == unicode.ToUpper(rune(s[i+1])) {
            s = s[:i] + s[i+2:]
            i -= 1
            if i < 0 {
                i = 0
            }
        } else {
            i += 1
        }
    }
    ans := ""
    for _, c := range s {
        if c != '*' {
            ans += string(c)
        }
    }
    return ans;
}