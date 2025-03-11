/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        if(recurse(head) == 1) {
            return new ListNode(1, head);
        }

        return head;
    }

    int recurse(ListNode* head) {
        head->val *= 2;

        if(head->next) 
            head->val += recurse(head->next);
        
        if(head->val > 9) {
            head->val %= 10;
            return 1;
        }

        return 0;
    }
};