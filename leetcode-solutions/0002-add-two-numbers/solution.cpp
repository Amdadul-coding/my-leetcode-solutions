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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* returning = new ListNode();
        ListNode* curr = returning;
        int carryout = 0;
        while(l1 != nullptr || l2 != nullptr || carryout != 0){
            int number1 = 0;
            int number2 = 0;
            if(l1 != nullptr){
                number1 = l1 -> val;
            }
            if(l2 != nullptr){
                number2 = l2 -> val;
            } 
            int number = number1 + number2 + carryout;
            int returnin = number%10;
            carryout = number / 10;
            ListNode* idk = new ListNode(returnin);
            curr -> next = idk;
            curr = curr -> next;
            if(l1 != nullptr){
                l1 = l1 -> next;
            }
            if(l2 != nullptr){
                l2 = l2 -> next;
            }
        }
        return returning -> next;
    }
};
