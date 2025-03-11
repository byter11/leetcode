/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    if recurse(root, target) {
        return nil
    }
    
    return root
}

func recurse(root *TreeNode, target int) bool {
    if root == nil {
        return false
    }

    if root.Left == nil && root.Right == nil && root.Val == target {
        return true
    }

    if recurse(root.Left, target) {
        root.Left = nil
    }

    if recurse(root.Right, target) {
        root.Right = nil
    }

    if root.Left == nil && root.Right == nil && root.Val == target {
        return true
    }

    return false
}