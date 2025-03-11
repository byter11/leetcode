/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun bstToGst(root: TreeNode?): TreeNode? {
        bstToGst(root, 0)
        return root
    }

    fun bstToGst(root: TreeNode?, rightSum: Int): Int {
        if(root == null) return 0

        root.`val` += rightSum
        if(root?.left == null && root?.right == null) return root.`val` - rightSum;
        root.`val` += bstToGst(root.right, rightSum)
        return root.`val` - rightSum + bstToGst(root.left, root.`val`)
    }
}