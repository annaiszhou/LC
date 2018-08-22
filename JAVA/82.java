/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	if (head == null) {
    		return head;
    	}
    	ListNode dummy = new ListNode(0);
    	dummy.next = head;
    	ListNode cur = dummy;
    	int value = 0;
    	while (cur.next != null && cur.next.next != null) {
    		if (cur.next.val == cur.next.next.val){
    			value = cur.next.val;
    			while (cur.next != null && cur.next.val == value) {
    				cur.next = cur.next.next;
    			}
    		}
    		else {
    			cur = cur.next;
    		}
    	}
        return dummy.next;
    }
}

#Runtime: 1 ms
#Your runtime beats 60.66 % of java submissions.
#space: O(1)
#time: O(2n)