func kthFactor(n int, k int) int {
    limit := int(math.Ceil(float64(n)/2))
    cur := 0

    for i := 1; i <= limit; i++ {
        if n % i == 0 {
            cur++
            if cur == k {
                return i
            }
        }
    }

    // handle n % n == 0 case
    cur++
    if cur == k {
        return n
    }

    return -1
}