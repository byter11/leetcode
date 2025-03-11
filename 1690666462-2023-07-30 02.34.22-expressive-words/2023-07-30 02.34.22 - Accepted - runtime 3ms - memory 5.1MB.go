import (
    "fmt"
)

func getGroups(s string) []string {
    grps := []string{}

    for _, char := range s {
        c := string(char)
        if len(grps) > 0 && string(grps[len(grps) - 1][0]) == c {
            grps[len(grps) - 1] += c
        } else {
            grps = append(grps, c)
        }
    }

    return grps
}

func expressiveWords(s string, words []string) int {
    groups := getGroups(s) 

    res := 0
    for _, word := range words {
        wordGroups := getGroups(word)
        if len(groups) != len(wordGroups) {
            continue
        }

        ok := true
        for i := 0; i < len(groups); i++ {
            if groups[i] == wordGroups[i] {
                continue
            }
            if len(groups[i]) < 3 || len(wordGroups[i]) > len(groups[i]) {
                ok = false
                break
            }
        }
        if ok {
            res++
        }
    } 
    return res
}
