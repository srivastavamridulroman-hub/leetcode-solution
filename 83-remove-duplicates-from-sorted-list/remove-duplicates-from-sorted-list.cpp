class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL) return head;

        ListNode* current = head;

        while(current != NULL && current->next != NULL) {
            if(current->val == current->next->val) {
                // skip duplicate
                current->next = current->next->next;
            } else {
                // move pointer
                current = current->next;
            }
        }

        return head;
    }
};