/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func distributeCoins(root *TreeNode) int {
    moves := 0
    distribute(root, &moves)
    return moves
}

func distribute(root *TreeNode, moves *int) int {
    if root == nil {
        return 0
    }
    
    if root.Left == nil && root.Right == nil {
        return root.Val - 1
    }

    leftRemainder := distribute(root.Left, moves)
    rightRemainder := distribute(root.Right, moves)

    root.Val += leftRemainder + rightRemainder
    *moves += int(math.Abs(float64(leftRemainder)) + math.Abs(float64(rightRemainder)))

    return root.Val - 1
}