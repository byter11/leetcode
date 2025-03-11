/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun mergeNodes(head: ListNode?): ListNode? {
        var cursor = head?.next

        while(cursor?.next != null) {
            if(cursor?.next?.`val` == 0) {
                cursor?.next = cursor?.next?.next
                cursor = cursor?.next
            } else {
                cursor.`val` += cursor?.next?.`val` ?: 0
                cursor?.next = cursor?.next?.next
            }
        }
        
        return head?.next
    }
}