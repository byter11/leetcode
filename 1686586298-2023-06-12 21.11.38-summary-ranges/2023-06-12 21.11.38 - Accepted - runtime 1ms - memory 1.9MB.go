import (
    "fmt"
    "strconv"
)

func summaryRanges(nums []int) []string {
    if len(nums) == 0 {
        return []string{}
    }
    i := nums[0]
    j := nums[0]
    result := []string{}

    for _, num := range nums[1:] {
        fmt.Println(num, j)
        if num - j != 1 {
            if i == j {
                result = append(result, strconv.Itoa(i))
            } else {    
                result = append(result, fmt.Sprintf("%d->%d", i, j))
            }
            i = num
        }
        j = num
    }
    if i == j {
        result = append(result, strconv.Itoa(i))
    } else {    
                result = append(result, fmt.Sprintf("%d->%d", i, j))
            }

    return result
}