func compareVersion(version1 string, version2 string) int {
    v1 := strings.Split(version1, ".")
    v2 := strings.Split(version2, ".")

    n := math.Min(float64(len(v1)), float64(len(v2)))
    for i := 0; i < int(n); i++ {
        a, _ := strconv.Atoi(v1[i])
        b, _ := strconv.Atoi(v2[i])

        if a > b {
            return 1
        }

        if b > a {
            return -1
        }
    }

    if len(v1) > len(v2) {
        for i := len(v2); i < len(v1); i++ {
            a, _ := strconv.Atoi(v1[i])
            if a != 0 {
                return 1
            }
        }
        return 0
    }

    if len(v2) > len(v1) {
        for i := len(v1); i < len(v2); i++ {
            a, _ := strconv.Atoi(v2[i])
            if a != 0 {
                return -1
            }
        }
        return 0
    }

    return 0
}